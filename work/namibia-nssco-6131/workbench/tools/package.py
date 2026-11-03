"""Seal, verify and export the local NSSCO Maths resource package. No network/DB."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import os
import tempfile

HOME = Path(__file__).resolve().parents[1]
LOCK = Path('services/api/data/resource_packages/namibia-nssco-6131.lock.json')


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def safe_path(root, name):
    path = PurePosixPath(name)
    if not name or path.is_absolute() or '..' in path.parts or '\\' in name or str(path) != name:
        raise ValueError(f'Invalid package path: {name}')
    root = root.resolve()
    result = root.joinpath(*path.parts)
    if not result.resolve().is_relative_to(root):
        raise ValueError(f'Path escapes package: {name}')
    if any(p.is_symlink() for p in (result, *result.parents) if p != root):
        raise ValueError(f'Symlink is not a package file: {name}')
    return result


def inventory(home):
    package = home / 'package'
    files = {}
    for p in sorted(package.rglob('*')):
        if '__pycache__' in p.parts or p.suffix in {'.pyc', '.pyo'}:
            continue
        name = p.relative_to(package).as_posix()
        safe_path(package, name)
        if p.is_file():
            files[name] = digest(p)
    return files


def content_summary(home):
    package = home / 'package'
    catalogue = json.loads((package / 'services/api/services/math_workbench/catalogue.json').read_text())
    bank = package / 'services/api/data/imports/nam-6131-nssco-2026/workbench-bank.json'
    frontend = json.loads((package / 'apps/web/components/MathsWorkbench/recipeCatalogue.json').read_text())
    if catalogue['summary']['sourceBankSha256'] != digest(bank) or frontend != catalogue['recipes']:
        raise ValueError('Rebuild the backend/frontend catalogue from the current bank before sealing')
    policy = json.loads((bank.parent / 'workbench-quality-policy.json').read_text())
    cards = json.loads(bank.read_text())['recipe_cards']
    recipe_ids = {c['recipe_id'] for c in cards}
    fingerprints = [c['question_snapshot']['fingerprint'] for c in cards]
    if recipe_ids & set(policy['retired_recipe_ids']):
        raise ValueError('Retired low-quality recipes cannot re-enter the active bank')
    if recipe_ids & set(policy.get('repair_pending_recipe_ids', [])):
        raise ValueError('Repair-pending recipes must remain outside the active bank')
    for card in cards:
        repaired=policy.get('repaired_recipe_versions',{}).get(card['recipe_id'])
        if repaired and card['generator_params']['recipe_version']!=repaired:
            raise ValueError('Older rejected recipe version cannot re-enter the active bank')
    for branch in policy.get('retired_branches', []):
        if any(c['recipe_id']==branch['recipe_id'] and
               c['question_snapshot'].get('source_branch',{}).get('skill')==branch['skill'] for c in cards):
            raise ValueError('Duplicate retired question branch in active bank')
    if len(fingerprints) != len(set(fingerprints)):
        raise ValueError('Duplicate question fingerprints in active bank')
    if recipe_ids != {r['recipeId'] for r in catalogue['recipes']}:
        raise ValueError('Active bank and assignment catalogue cover different recipes')
    if any(r['availability'] != 'available' for r in catalogue['recipes']):
        raise ValueError('Held content belongs outside the active catalogue')
    actual = {'recipeSettings': len(recipe_ids), 'savedExamples': len(cards), 'assignmentTypes': len(catalogue['recipes'])}
    if any(catalogue['summary'].get(k) != v for k,v in actual.items()):
        raise ValueError('Catalogue counts do not match active content')
    return catalogue['summary']


def seal(home=HOME):
    path = home / 'manifest.json'
    manifest = json.loads(path.read_text())
    files = inventory(home)
    if not files:
        raise ValueError('Empty resource package')
    for name in files:
        safe_path(home / 'package', name)
    manifest['files'] = files
    manifest['summary'] = content_summary(home)
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
    return len(files)


def verify(home=HOME):
    manifest = json.loads((home / 'manifest.json').read_text())
    if manifest['schema_version'] != 1 or manifest['package_id'] != 'namibia-nssco-6131':
        raise ValueError('Unsupported subject package')
    if not manifest['files']:
        raise ValueError('Empty resource package')
    for name in manifest['files']:
        safe_path(home / 'package', name)
    actual = inventory(home)
    if actual != manifest['files']:
        changed = sorted(k for k in actual.keys() | manifest['files'].keys()
                         if actual.get(k) != manifest['files'].get(k))
        raise ValueError(f'Package differs from manifest; review and seal changes: {changed[:8]}')
    if manifest['summary'] != content_summary(home):
        raise ValueError('Manifest summary differs from the content catalogue')
    return manifest


def atomic_write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(dir=path.parent, prefix='.resource-')
    try:
        with os.fdopen(descriptor, 'wb') as stream:
            stream.write(content)
        os.chmod(temporary, 0o644)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def export(target, home=HOME, check=False, remove=()):
    manifest = verify(home)
    target = target.resolve()
    lock_path = safe_path(target, LOCK.as_posix())
    old = json.loads(lock_path.read_text()) if lock_path.exists() else None
    if old and old['package_id'] != manifest['package_id']:
        raise ValueError('Destination lock belongs to another subject')
    old_files = old['files'] if old else {}
    removals = old_files.keys() - manifest['files'].keys()
    if set(remove) != removals:
        raise ValueError('Removing deployed files requires an explicit archive review and exact --remove list')
    removed_paths = []
    for name in sorted(removals):
        dest = safe_path(target, name)
        if not dest.is_file() or digest(dest) != old_files[name]:
            raise ValueError(f'Destination has local edits: {name}')
        removed_paths.append(dest)
    pending = []
    for name, checksum in manifest['files'].items():
        dest = safe_path(target, name)
        current = digest(dest) if dest.exists() else None
        if check:
            if current != checksum:
                raise ValueError(f'Deployment copy differs: {name}')
        elif current != checksum:
            # Initial migration cannot overwrite a different existing file.
            # Subsequent imports can only replace the previously locked bytes.
            if (name in old_files and current != old_files[name]) or (name not in old_files and current is not None):
                raise ValueError(f'Destination has local edits: {name}')
            pending.append((dest, safe_path(home / 'package', name)))
    lock = {**manifest, 'manifest_sha256': digest(home / 'manifest.json')}
    if check:
        if old != lock:
            raise ValueError('Deployment lock differs from resource manifest')
    else:
        # All sources, destinations and conflicts are checked before the first write.
        # Individual writes are atomic; export into an inactive checkout before deploy.
        for dest, source in pending:
            atomic_write(dest, source.read_bytes())
        for dest in removed_paths:
            dest.unlink()
        atomic_write(lock_path, (json.dumps(lock, indent=2, ensure_ascii=False) + '\n').encode())
    return len(manifest['files'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['seal', 'verify', 'export', 'check'])
    parser.add_argument('--target', type=Path, help='Inactive YYeni application checkout')
    parser.add_argument('--remove', action='append', default=[], help='Exact previously locked path explicitly approved for removal')
    args = parser.parse_args()
    if args.action in {'export', 'check'}:
        if not args.target or not (args.target / 'services/api').is_dir():
            parser.error('--target must be a YYeni application checkout')
        count = export(args.target, check=args.action == 'check', remove=args.remove)
    elif args.action == 'seal':
        count = seal()
    else:
        count = len(verify()['files'])
    print(f'{args.action}: {count} files')


if __name__ == '__main__':
    main()

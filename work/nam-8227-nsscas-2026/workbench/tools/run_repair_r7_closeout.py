"""Reuse the full R7 pipeline, adding only the named close-out checker.

A single rebuild is not a double-build proof. The relocated helper runs two
independent single rebuilds and compares both to the unchanged author checkout.
"""
import argparse
import json
from pathlib import Path
import run_repair_r7 as prior
from analysis_sources import ROOT,WB,digest,write

BASE_HASHES=prior.hashes
CHECKER='check_repair_r7_closeout.py'
CHECKERS=[*prior.CHECKERS,CHECKER]
PROOF_PREFIXES=('single-rebuild','negative-only','rebuild-verification','fresh-copy',
                'freshmanifest','mismatch')
PROOF_PARTS={'rebuild-drift','fresh-copy-copies'}


def is_proof_path(path):
    """The same predicate is used by the runner and fresh-copy helper."""
    p=Path(path)
    return bool(set(p.parts)&PROOF_PARTS) or p.name in prior.PROOF_NAMES or p.name.startswith(PROOF_PREFIXES)


def steps():
    names=prior.steps()
    index=names.index('check_repair_r7.py')
    return [*names[:index+1],CHECKER,*names[index+1:]]


def hashes():
    result={p:sha for p,sha in BASE_HASHES().items() if not is_proof_path(p)}
    directory=WB/'checks/r7-closeout'
    for path in sorted([*directory.rglob('*.json'),*directory.rglob('*.md')]):
        if path.is_file() and not is_proof_path(path):
            result[str(path.relative_to(ROOT))]=digest(path)
    return dict(sorted(result.items()))


def run_steps(names,counter):
    if names==CHECKERS:
        # Reuse the old checker-only route without accidentally adding producer
        # commands or the two full-build trailing stage checks.
        return [*prior.run_steps(prior.CHECKERS,counter),prior.command(CHECKER,counter)]
    return prior.run_steps(names,counter)


def previous_negatives():
    # The retained 38 fixtures check unchanged outputs after every failure.
    # Give that established implementation this round's complete projection.
    original=prior.hashes
    prior.hashes=hashes
    try:return prior.previous_negatives()
    finally:prior.hashes=original


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--single-rebuild',action='store_true')
    parser.add_argument('--negative-only',action='store_true')
    parser.add_argument('--print-hashes',action='store_true',help=argparse.SUPPRESS)
    args=parser.parse_args()
    if args.print_hashes:
        assert not(args.single_rebuild or args.negative_only),'hash projection mode cannot rebuild'
        print(json.dumps(hashes(),sort_keys=True));return
    assert not(args.single_rebuild and args.negative_only),'choose a single mode'
    counter=[0]
    if args.negative_only:
        commands=run_steps(CHECKERS,counter);negative=previous_negatives()
        write(WB/'checks/r7-closeout/negative-only-r7-closeout.json',dict(
            status='Current canonical close-out checkers and retained/new negative suites passed; no rebuild performed.',
            commands=commands,previous_seeded_negative_results=negative,
            previous_seeded_negative_count=len(negative),
            limits='Structural checks only; no fresh-copy, educational or production acceptance.'))
        print(json.dumps(dict(checkers='pass',established_subprocess_negatives_rejected=len(negative)),indent=2),flush=True)
        return
    first=run_steps(steps(),counter);before=hashes()
    if args.single_rebuild:
        write(WB/'checks/r7-closeout/single-rebuild-r7-closeout.json',dict(
            status='One full author close-out rebuild passed; not double-rebuild proof.',
            commands=first,output_hashes=before,outputs_compared=len(before),
            limits='No independent educational, runtime or production acceptance.'))
        print(json.dumps(dict(single_rebuild='pass',commands=len(first),outputs=len(before)),indent=2),flush=True)
        return
    first_bytes={p:(ROOT/p).read_bytes() for p in before if Path(p).suffix in ['.json','.md']}
    second=run_steps(steps(),counter);after=hashes()
    changed=[p for p in sorted(set(before)|set(after)) if before.get(p)!=after.get(p)]
    if changed:
        folder=WB/'checks/r7-closeout/rebuild-drift';folder.mkdir(parents=True,exist_ok=True)
        for n,path in enumerate(changed):
            if path in first_bytes:(folder/f'{n:03d}-first-{Path(path).name}').write_bytes(first_bytes[path])
            if (ROOT/path).is_file():(folder/f'{n:03d}-second-{Path(path).name}').write_bytes((ROOT/path).read_bytes())
        write(folder/'manifest.json',dict(status='FAILED: nondeterministic close-out rebuild',changed_paths=changed,
            first_hashes={p:before.get(p)for p in changed},second_hashes={p:after.get(p)for p in changed}))
    assert not changed,('nondeterministic R7 close-out outputs',changed)
    negative=previous_negatives()
    write(WB/'checks/r7-closeout/rebuild-verification-r7-closeout.json',dict(
        first_rebuild=first,second_rebuild=second,outputs_compared=len(after),identical=True,
        changed_paths=[],output_hashes=after,previous_seeded_negative_results=negative,
        previous_seeded_negative_count=len(negative),
        limits='Two deterministic author rebuilds in one checkout; independent fresh copies and educational acceptance remain separate.'))
    print(json.dumps(dict(rebuilds='two passed',outputs_byte_identical=len(after),established_subprocess_negatives_rejected=len(negative)),indent=2),flush=True)


if __name__=='__main__':main()

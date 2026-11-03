"""Conflict and integrity tests for local package exports; no application/DB imports."""
import json
from pathlib import Path
import tempfile
import unittest

import package


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.home = self.root / 'resources'
        self.target = self.root / 'app'
        self.target.mkdir()
        self.content = self.home / 'package'
        self.generator = 'services/api/services/math_generators/example.py'
        self.write(self.generator, 'original generator\n')
        bank = 'services/api/data/imports/nam-6131-nssco-2026/workbench-bank.json'
        self.write(bank, '{"recipe_cards": []}')
        self.write('services/api/data/imports/nam-6131-nssco-2026/workbench-quality-policy.json', '{"retired_recipe_ids": []}')
        summary = {'sourceBankSha256': package.digest(self.content / bank), 'recipeSettings': 0, 'savedExamples': 0, 'assignmentTypes': 0}
        self.write('services/api/services/math_workbench/catalogue.json', json.dumps({'summary': summary, 'recipes': []}))
        self.write('apps/web/components/MathsWorkbench/recipeCatalogue.json', '[]')
        (self.home / 'manifest.json').write_text(json.dumps({
            'schema_version': 1, 'package_id': 'namibia-nssco-6131', 'files': {}}))
        package.seal(self.home)

    def write(self, name, text):
        path = self.content / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def export(self, check=False):
        return package.export(self.target, self.home, check=check)

    def test_first_export_and_repeat_are_identical(self):
        self.assertEqual(self.export(), 5)
        before = (self.target / package.LOCK).read_bytes()
        self.assertEqual(self.export(check=True), 5)
        self.export()
        self.assertEqual((self.target / package.LOCK).read_bytes(), before)

    def test_unsealed_source_change_is_rejected_before_write(self):
        self.write(self.generator, 'changed')
        with self.assertRaisesRegex(ValueError, 'differs from manifest'):
            self.export()
        self.assertFalse((self.target / package.LOCK).exists())
        self.assertEqual(list(self.target.iterdir()), [])

    def test_sealed_update_replaces_previously_locked_copy(self):
        self.export()
        self.write(self.generator, 'reviewed update')
        package.seal(self.home)
        with self.assertRaises(ValueError):
            self.export(check=True)
        self.export()
        self.assertEqual((self.target / self.generator).read_text(), 'reviewed update')
        self.export(check=True)

    def test_destination_edit_blocks_whole_export(self):
        self.export()
        old_lock = (self.target / package.LOCK).read_bytes()
        self.write(self.generator, 'new source')
        self.write('new-file.txt', 'must not be written')
        package.seal(self.home)
        (self.target / self.generator).write_text('local edit')
        with self.assertRaisesRegex(ValueError, 'local edits'):
            self.export()
        self.assertFalse((self.target / 'new-file.txt').exists())
        self.assertEqual((self.target / package.LOCK).read_bytes(), old_lock)

    def test_initial_export_cannot_overwrite_untracked_different_file(self):
        dest = self.target / self.generator
        dest.parent.mkdir(parents=True)
        dest.write_text('pre-existing')
        with self.assertRaisesRegex(ValueError, 'local edits'):
            self.export()
        self.assertEqual(dest.read_text(), 'pre-existing')

    def test_file_removal_requires_separate_archive_review(self):
        self.export()
        (self.content / self.generator).unlink()
        package.seal(self.home)
        with self.assertRaisesRegex(ValueError, 'archive review'):
            self.export()
        self.assertTrue((self.target / self.generator).exists())

    def test_escaping_path_in_manifest_is_rejected(self):
        manifest = json.loads((self.home / 'manifest.json').read_text())
        manifest['files']['../outside'] = 'a' * 64
        (self.home / 'manifest.json').write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'Invalid package path'):
            self.export()
        self.assertEqual(list(self.target.iterdir()), [])

    def test_explicit_removal_deletes_only_the_locked_file(self):
        self.export()
        (self.content / self.generator).unlink()
        package.seal(self.home)
        package.export(self.target, self.home, remove=[self.generator])
        self.assertFalse((self.target / self.generator).exists())
        self.export(check=True)

    def test_removal_refuses_locally_edited_deployment_copy(self):
        self.export()
        (self.content / self.generator).unlink()
        package.seal(self.home)
        (self.target / self.generator).write_text('local edit')
        with self.assertRaisesRegex(ValueError, 'local edits'):
            package.export(self.target, self.home, remove=[self.generator])
        self.assertEqual((self.target / self.generator).read_text(), 'local edit')

    def test_symlink_source_is_rejected_even_when_inside_package(self):
        (self.content / 'linked.txt').symlink_to(self.content / self.generator)
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            package.seal(self.home)

    def test_symlink_destination_is_rejected(self):
        outside = self.root / 'outside'
        outside.mkdir()
        (self.target / 'services').symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'escapes package'):
            self.export()
        self.assertEqual(list(outside.iterdir()), [])

    def test_stale_catalogue_is_rejected_even_after_resealing(self):
        self.write('services/api/data/imports/nam-6131-nssco-2026/workbench-bank.json', '{"changed": true}')
        with self.assertRaisesRegex(ValueError, 'Rebuild'):
            package.seal(self.home)

    def set_active_content(self, cards, recipes, retired=()):
        bank='services/api/data/imports/nam-6131-nssco-2026/workbench-bank.json'
        self.write(bank,json.dumps({'recipe_cards':cards}))
        summary={'sourceBankSha256':package.digest(self.content/bank),
                 'recipeSettings':len({c['recipe_id'] for c in cards}),
                 'savedExamples':len(cards),'assignmentTypes':len(recipes)}
        self.write('services/api/services/math_workbench/catalogue.json',json.dumps({'summary':summary,'recipes':recipes}))
        self.write('apps/web/components/MathsWorkbench/recipeCatalogue.json',json.dumps(recipes))
        self.write('services/api/data/imports/nam-6131-nssco-2026/workbench-quality-policy.json',json.dumps({'retired_recipe_ids':list(retired)}))

    def test_duplicate_examples_cannot_be_sealed(self):
        card={'recipe_id':'example','question_snapshot':{'fingerprint':'same-question'}}
        self.set_active_content([card,card],[{'recipeId':'example','availability':'available'}])
        with self.assertRaisesRegex(ValueError,'Duplicate question'):
            package.seal(self.home)

    def test_rejected_recipes_cannot_be_sealed(self):
        card={'recipe_id':'retired','question_snapshot':{'fingerprint':'question'}}
        self.set_active_content([card],[{'recipeId':'retired','availability':'available'}],retired=['retired'])
        with self.assertRaisesRegex(ValueError,'Retired low-quality'):
            package.seal(self.home)

    def test_held_recipes_do_not_belong_in_active_catalogue(self):
        card={'recipe_id':'example','question_snapshot':{'fingerprint':'question'}}
        self.set_active_content([card],[{'recipeId':'example','availability':'held'}])
        with self.assertRaisesRegex(ValueError,'Held content'):
            package.seal(self.home)

    def test_repair_queue_cannot_be_sealed_into_active_content(self):
        card={'recipe_id':'pending','question_snapshot':{'fingerprint':'question'}}
        self.set_active_content([card],[{'recipeId':'pending','availability':'available'}])
        self.write('services/api/data/imports/nam-6131-nssco-2026/workbench-quality-policy.json',
                   json.dumps({'retired_recipe_ids':[], 'repair_pending_recipe_ids':['pending']}))
        with self.assertRaisesRegex(ValueError,'Repair-pending'):
            package.seal(self.home)

    def test_repaired_recipe_cannot_be_replaced_with_its_old_version(self):
        card={'recipe_id':'repaired','generator_params':{'recipe_version':7},'question_snapshot':{'fingerprint':'question'}}
        self.set_active_content([card],[{'recipeId':'repaired','availability':'available'}])
        self.write('services/api/data/imports/nam-6131-nssco-2026/workbench-quality-policy.json',
                   json.dumps({'retired_recipe_ids':[], 'repaired_recipe_versions':{'repaired':9}}))
        with self.assertRaisesRegex(ValueError,'Older rejected recipe version'):
            package.seal(self.home)


if __name__ == '__main__':
    unittest.main()

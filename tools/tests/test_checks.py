"""Regression tests for template integration and relocated content utilities."""

from __future__ import annotations

import contextlib
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
VALID_PROJECT = '''---
title: "Example"
date: "2026-11-24"
imageUrl: "example/cover.jpg"
subtitle: "An example project"
bulletPoints: []
---
'''


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class FrontMatterTests(unittest.TestCase):
    def run_checker(self, directory, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPTS / "check_frontmatter.py"),
             "--projects-dir", str(directory), *args],
            cwd=directory.parent, capture_output=True, text=True,
        )

    def test_strict_mode_fails_for_bad_metadata(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            (directory / "bad.md").write_text(
                VALID_PROJECT.replace('title: "Example"', 'title: "<b>Example</b>"')
                .replace('date: "2026-11-24"', 'date: 2026-11-24')
                .replace('subtitle: "An example project"', 'title: "<b>Duplicate</b>"'),
                encoding="utf-8",
            )
            result = self.run_checker(directory, "--strict")
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            for issue in ("duplicate key", "missing required field 'subtitle'", "HTML tag", "date should be quoted"):
                self.assertIn(issue, result.stdout)
            self.assertEqual(self.run_checker(directory).returncode, 0)

    def test_strict_mode_accepts_valid_metadata(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            (directory / "valid.md").write_text(VALID_PROJECT, encoding="utf-8")
            result = self.run_checker(directory, "--strict")
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("1 files", result.stdout)

    def test_missing_and_empty_directories_fail(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.assertEqual(self.run_checker(directory, "--strict").returncode, 2)
            self.assertEqual(self.run_checker(directory / "missing", "--strict").returncode, 2)


class UtilityPathTests(unittest.TestCase):
    def make_project_tree(self, temporary):
        root = Path(temporary)
        script = root / "tools" / "scripts" / "utility.py"
        projects = root / "content" / "projects"
        projects.mkdir(parents=True)
        return script, projects

    def test_normalizer_uses_repository_root_after_move(self):
        module = load_script("normalize_frontmatter")
        with tempfile.TemporaryDirectory() as temporary:
            script, projects = self.make_project_tree(temporary)
            project = projects / "example.md"
            project.write_text(VALID_PROJECT.replace('title: "Example"', 'title: "<b>Example</b>"'), encoding="utf-8")
            with patch.object(module, "__file__", str(script)), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(module.main(), 0)
            self.assertEqual(project.read_text(encoding="utf-8"), VALID_PROJECT)

    def test_converter_uses_repository_root_after_move(self):
        module = load_script("convert_image_links")
        with tempfile.TemporaryDirectory() as temporary:
            script, projects = self.make_project_tree(temporary)
            project = projects / "example.md"
            project.write_text('![Cover](/img/example/cover.jpg)\n', encoding="utf-8")
            with patch.object(module, "__file__", str(script)), patch.object(sys, "argv", [str(script)]), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(module.main(), 0)
            self.assertEqual(project.read_text(encoding="utf-8"), '{{< img src="example/cover.jpg" alt="Cover" >}}\n')


class IntegrationTests(unittest.TestCase):
    def test_documentation_scope_preserves_site_content(self):
        for name in ("check_acronyms", "check_links"):
            with self.subTest(check=name), tempfile.TemporaryDirectory() as temporary:
                module = load_script(name)
                root = Path(temporary)
                files = ["README.md", "docs/example.md", "content/projects/example.md", "TODO.md"]
                for filename in files:
                    path = root / filename
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_text("Example\n", encoding="utf-8")
                result = subprocess.CompletedProcess([], 0, stdout="\0".join(files) + "\0")
                with patch.object(module, "ROOT", root), patch.object(module.subprocess, "run", return_value=result):
                    found = {path.relative_to(root).as_posix() for path in module.markdown_files()}
                expected = {"README.md", "docs/example.md"}
                if name == "check_links":
                    expected.add("TODO.md")
                self.assertEqual(found, expected)

    def test_runner_enforces_strict_mode_and_runs_remaining_checks(self):
        module = load_script("run_checks")
        results = [subprocess.CompletedProcess([], 1), subprocess.CompletedProcess([], 0)]
        with patch.object(sys, "argv", ["run_checks.py", "frontmatter", "links"]), patch.object(module.subprocess, "run", side_effect=results) as run, contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(module.main(), 1)
        self.assertEqual(run.call_count, 2)
        self.assertIn("--strict", run.call_args_list[0].args[0])
        self.assertEqual(run.call_args_list[0].kwargs["cwd"], SCRIPTS.parents[1])

    def test_runner_works_from_outside_repository(self):
        with tempfile.TemporaryDirectory() as temporary:
            result = subprocess.run(
                [sys.executable, str(SCRIPTS / "run_checks.py"), "frontmatter"],
                cwd=temporary, capture_output=True, text=True,
            )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("Passed: frontmatter", result.stdout)


if __name__ == "__main__":
    unittest.main()

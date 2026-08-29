"""Smoke tests for the AnimeBench package."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout

from animebench import __version__
from animebench.cli import main


class CliTests(unittest.TestCase):
    def test_package_has_version(self) -> None:
        self.assertEqual(__version__, "0.1.0")

    def test_placeholder_cli_runs(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            exit_code = main([])

        self.assertEqual(exit_code, 0)
        self.assertIn("AnimeBench is scaffolded", output.getvalue())


if __name__ == "__main__":
    unittest.main()

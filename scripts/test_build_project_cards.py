import tempfile
import json
import unittest
import subprocess
import sys
from pathlib import Path

from build_project_cards import verify_accessibility


class CardAccessibilityTests(unittest.TestCase):
    def test_generated_card_slugs_can_be_listed(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("build_project_cards.py")), "--list"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("folio-static-site\n", result.stdout)
        self.assertIn("omarchy-counter\n", result.stdout)

    def test_generated_card_slugs_can_be_listed_as_json(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("build_project_cards.py")), "--list", "--json"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        slugs = json.loads(result.stdout)
        self.assertEqual(len(slugs), 13)
        self.assertIn("cinesearch-rag-engine", slugs)

    def test_one_card_can_be_checked_by_slug(self):
        result = subprocess.run(
            [
                sys.executable,
                str(Path(__file__).with_name("build_project_cards.py")),
                "--check",
                "--only",
                "folio-static-site",
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Verified 1 project-specific SVG card", result.stdout)

    def test_multiple_cards_can_be_checked_by_slug(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("build_project_cards.py")), "--check", "--only", "folio-static-site", "--only", "orbit-asteroids-game"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Verified 2 project-specific SVG card", result.stdout)

    def test_active_svg_content_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            for active in ('<script>alert(1)</script>', '<g onclick="alert(1)"/>'):
                path = Path(directory) / "active.svg"
                path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc>{active}</svg>')
                with self.subTest(active=active), self.assertRaises(SystemExit):
                    verify_accessibility(path)

    def test_external_svg_references_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            for reference in (
                "https://example.com/image.png",
                "data:image/png;base64,AAAA",
                "javascript:alert(1)",
                "//example.com/image.png",
                "ftp://example.com/image.png",
                "file:///tmp/image.png",
                "blob:https://example.com/id",
                "relative.png",
            ):
                path = Path(directory) / "external.svg"
                path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc><image href="{reference}"/></svg>')
                with self.subTest(reference=reference), self.assertRaises(SystemExit):
                    verify_accessibility(path)

    def test_only_existing_local_svg_references_are_allowed(self):
        with tempfile.TemporaryDirectory() as directory:
            valid = Path(directory) / "valid.svg"
            valid.write_text('<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc><defs><path id="shape"/></defs><use href="#shape" fill="url(#shape)"/></svg>')
            verify_accessibility(valid)
            for content in (
                '<image href="#missing"/>',
                '<path fill="url(https://example.com/fill.svg)"/>',
                '<foreignObject/>',
            ):
                path = Path(directory) / "unsafe.svg"
                path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc>{content}</svg>')
                with self.subTest(content=content), self.assertRaises(SystemExit):
                    verify_accessibility(path)

    def test_empty_accessible_text_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            for empty in ("title", "desc"):
                path = Path(directory) / f"{empty}.svg"
                title = "   " if empty == "title" else "Card"
                desc = "   " if empty == "desc" else "Description"
                path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">{desc}</desc></svg>')
                with self.subTest(empty=empty), self.assertRaises(SystemExit):
                    verify_accessibility(path)

    def test_duplicate_svg_ids_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "card.svg"
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc><g id="desc"/></svg>')
            with self.assertRaises(SystemExit):
                verify_accessibility(path)


if __name__ == "__main__":
    unittest.main()

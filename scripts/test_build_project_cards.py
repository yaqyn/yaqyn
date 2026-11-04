import tempfile
import json
import unittest
import subprocess
import sys
from unittest.mock import patch
from pathlib import Path

from build_project_cards import verify_accessibility


class CardAccessibilityTests(unittest.TestCase):
    def test_root_must_be_a_namespaced_svg_element(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "card.svg"
            for root in ("div", "svg"):
                path.write_text(f'<{root} width="132" height="132" viewBox="0 0 132 132" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc></{root}>')
                with self.subTest(root=root), self.assertRaises(SystemExit):
                    verify_accessibility(path)

    def test_failed_card_replace_preserves_existing_output(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "folio-static-site.svg"
            path.write_text("approved")
            with patch("build_project_cards.os.replace", side_effect=OSError("blocked")):
                from build_project_cards import card
                with patch("build_project_cards.OUT", Path(directory)):
                    with self.assertRaises(OSError):
                        card("folio-static-site", "Folio", "Description", "#000", "#fff", "")
            self.assertEqual(path.read_text(), "approved")
            self.assertEqual([item.name for item in Path(directory).iterdir()], ["folio-static-site.svg"])

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

    def test_card_checks_can_report_json(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("build_project_cards.py")), "--check", "--only", "folio-static-site", "--json"],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), {"action": "verified", "cards": ["folio-static-site"], "count": 1})

    def test_multiple_cards_can_be_checked_by_slug(self):
        result = subprocess.run(
            [sys.executable, str(Path(__file__).with_name("build_project_cards.py")), "--check", "--only", "folio-static-site", "--only", "orbit-asteroids-game"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Verified 2 project-specific SVG card", result.stdout)

    def test_card_can_be_built_in_an_alternate_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [sys.executable, str(Path(__file__).with_name("build_project_cards.py")),
                 "--only", "folio-static-site", "--output-dir", directory],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((Path(directory) / "folio-static-site.svg").is_file())

    def test_active_svg_content_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            for active in ('<script>alert(1)</script>', '<g onclick="alert(1)"/>'):
                path = Path(directory) / "active.svg"
                path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc>{active}</svg>')
                with self.subTest(active=active), self.assertRaises(SystemExit):
                    verify_accessibility(path)

    def test_svg_animation_elements_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            for animation in ("animate", "animateMotion", "animateTransform", "set"):
                path = Path(directory) / "animated.svg"
                path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="132" height="132" viewBox="0 0 132 132" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc><{animation} attributeName="opacity"/></svg>')
                with self.subTest(animation=animation), self.assertRaises(SystemExit):
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

    def test_document_type_declarations_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "declared.svg"
            path.write_text('<!DOCTYPE svg><svg xmlns="http://www.w3.org/2000/svg" width="132" height="132" viewBox="0 0 132 132" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc></svg>')
            with self.assertRaises(SystemExit):
                verify_accessibility(path)

    def test_only_existing_local_svg_references_are_allowed(self):
        with tempfile.TemporaryDirectory() as directory:
            valid = Path(directory) / "valid.svg"
            valid.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="132" height="132" viewBox="0 0 132 132" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc><defs><path id="shape"/></defs><use href="#shape" fill="url(#shape)"/></svg>')
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

    def test_cards_require_one_direct_title_and_description(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "card.svg"
            for duplicate in ("<title>Second</title>", "<desc>Second description</desc>"):
                path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="132" height="132" viewBox="0 0 132 132" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc>{duplicate}</svg>')
                with self.subTest(duplicate=duplicate), self.assertRaises(SystemExit):
                    verify_accessibility(path)

    def test_duplicate_svg_ids_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "card.svg"
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc><g id="desc"/></svg>')
            with self.assertRaises(SystemExit):
                verify_accessibility(path)

    def test_card_geometry_is_required(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "card.svg"
            for geometry in (
                'width="0" height="132" viewBox="0 0 132 132"',
                'width="132" height="132" viewBox="0 0 64 64"',
                '',
            ):
                path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" {geometry} role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc></svg>')
                with self.subTest(geometry=geometry), self.assertRaises(SystemExit):
                    verify_accessibility(path)


if __name__ == "__main__":
    unittest.main()

import tempfile
import unittest
from pathlib import Path

from build_project_cards import verify_accessibility


class CardAccessibilityTests(unittest.TestCase):
    def test_active_svg_content_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            for active in ('<script>alert(1)</script>', '<g onclick="alert(1)"/>'):
                path = Path(directory) / "active.svg"
                path.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="title desc"><title id="title">Card</title><desc id="desc">Description</desc>{active}</svg>')
                with self.subTest(active=active), self.assertRaises(SystemExit):
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

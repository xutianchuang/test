import tempfile
import unittest
from pathlib import Path

from generate_image import generate_svg


class TestGenerateImage(unittest.TestCase):
    def test_generate_svg_writes_svg_content(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            output = Path(tmp_dir) / "img.svg"
            generate_svg(output, 4, 3)

            self.assertTrue(output.exists())
            content = output.read_text(encoding="utf-8")

            self.assertIn('<svg xmlns="http://www.w3.org/2000/svg" width="4" height="3"', content)

    def test_generate_svg_rejects_non_positive_dimensions(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            output = Path(tmp_dir) / "img.svg"
            with self.assertRaises(ValueError):
                generate_svg(output, 0, 5)
            with self.assertRaises(ValueError):
                generate_svg(output, 5, 0)
            with self.assertRaises(ValueError):
                generate_svg(output, -1, 5)
            with self.assertRaises(ValueError):
                generate_svg(output, 5, -1)


if __name__ == "__main__":
    unittest.main()

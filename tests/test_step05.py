import importlib.util
import unittest
from pathlib import Path

from tests.helpers import load_module_from_step


class TestStep05(unittest.TestCase):
    def setUp(self):
        self.module = load_module_from_step("step-05-documentation-generation")
        self.step_dir = Path(__file__).resolve().parent.parent / "step-05-documentation-generation"

    def test_runtime_behavior(self):
        self.assertEqual(self.module.chunk_list([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(self.module.moving_average([1.0, 2.0, 3.0], 2), [1.5, 2.5])

    def test_docstrings_present(self):
        self.assertIsNotNone(self.module.chunk_list.__doc__)
        self.assertIsNotNone(self.module.moving_average.__doc__)
        self.assertIn("Parameters", self.module.chunk_list.__doc__ or "")
        self.assertIn("Returns", self.module.chunk_list.__doc__ or "")

    def test_usage_file_filled(self):
        usage_text = (self.step_dir / "USAGE.md").read_text(encoding="utf-8")
        self.assertNotIn("TODO", usage_text)


if __name__ == "__main__":
    unittest.main()
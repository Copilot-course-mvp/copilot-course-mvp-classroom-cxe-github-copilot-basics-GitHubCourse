import ast
import unittest
from pathlib import Path

from tests.helpers import load_module_from_step


class TestStep03(unittest.TestCase):
    def setUp(self):
        self.module = load_module_from_step("step-03-refactor")
        self.file_path = Path(__file__).resolve().parent.parent / "step-03-refactor" / "exercise.py"

    def test_behavior(self):
        self.assertEqual(self.module.checkout_total([10, 10], 0), 20.0)
        self.assertEqual(self.module.invoice_total([10, 10], 50), 10.0)
        self.assertEqual(self.module.checkout_total([], 10), 0.0)
        self.assertEqual(self.module.invoice_total([5], 100), 0.0)

    def test_refactor_helper_exists(self):
        source = self.file_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        function_names = [node.name for node in tree.body if isinstance(node, ast.FunctionDef)]
        self.assertIn("apply_discount", function_names, "Expected helper function apply_discount")


if __name__ == "__main__":
    unittest.main()
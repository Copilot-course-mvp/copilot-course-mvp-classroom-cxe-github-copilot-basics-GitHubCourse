import unittest

from tests.helpers import load_module_from_step


class TestStep01(unittest.TestCase):
    def setUp(self):
        self.module = load_module_from_step("step-01-code-completion")

    def test_normalize_username(self):
        self.assertEqual(self.module.normalize_username("  Alice Smith  "), "alice_smith")
        self.assertEqual(self.module.normalize_username("__B@b__"), "bb")
        self.assertEqual(self.module.normalize_username("John   Doe"), "john_doe")

    def test_build_slug(self):
        self.assertEqual(self.module.build_slug("Hello, World!"), "hello-world")
        self.assertEqual(self.module.build_slug("  AI   +  Copilot 101  "), "ai-copilot-101")
        self.assertEqual(self.module.build_slug("***"), "")


if __name__ == "__main__":
    unittest.main()
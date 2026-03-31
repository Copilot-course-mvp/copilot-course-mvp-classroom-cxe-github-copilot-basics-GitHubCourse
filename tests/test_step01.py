import unittest

from tests.helpers import load_module_from_step


class TestStep01(unittest.TestCase):
    def setUp(self):
        self.module = load_module_from_step("step-01-code-completion")

    def test_normalize_username(self):
        self.assertEqual(
            self.module.normalize_username("  Alice Smith  "),
            "alice_smith",
            "Missing rule: trim outer whitespace, lowercase, and replace spaces with one underscore.",
        )
        self.assertEqual(
            self.module.normalize_username("__B@b__"),
            "bb",
            "Missing rule: remove non [a-z0-9_] characters and strip leading/trailing underscores.",
        )
        self.assertEqual(
            self.module.normalize_username("John   Doe"),
            "john_doe",
            "Missing rule: collapse multiple spaces into one underscore.",
        )
        self.assertEqual(
            self.module.normalize_username("!!!"),
            "",
            "Missing edge case: return an empty string when all characters are filtered out.",
        )
        self.assertEqual(
            self.module.normalize_username("\t  Jane\nDoe  \t"),
            "jane_doe",
            "Missing edge case: treat tabs/newlines as whitespace when normalizing.",
        )
        self.assertEqual(
            self.module.normalize_username("___"),
            "",
            "Missing edge case: strip underscores from both ends after normalization.",
        )
        self.assertEqual(
            self.module.normalize_username("A__B   C"),
            "a_b_c",
            "Missing edge case: collapse repeated underscores into a single underscore.",
        )

    def test_normalize_username_type_error(self):
        with self.assertRaisesRegex(
            TypeError,
            "name must be a string",
            msg="Missing edge case: reject non-string input with a clear TypeError.",
        ):
            self.module.normalize_username(None)
        

    def test_build_slug(self):
        self.assertEqual(
            self.module.build_slug("Hello, World!"),
            "hello-world",
            "Missing rule: lowercase and replace punctuation boundaries with '-'.",
        )
        self.assertEqual(
            self.module.build_slug("  AI   +  Copilot 101  "),
            "ai-copilot-101",
            "Missing rule: collapse non-alphanumeric sequences into a single '-'.",
        )
        self.assertEqual(
            self.module.build_slug("***"),
            "",
            "Missing edge case: return an empty slug when no letters/digits exist.",
        )
        self.assertEqual(
            self.module.build_slug("Python___Rocks!!! 2026"),
            "python-rocks-2026",
            "Missing edge case: underscores and punctuation should become single '-'.",
        )
        self.assertEqual(
            self.module.build_slug("---Start Middle End---"),
            "start-middle-end",
            "Missing edge case: strip leading/trailing '-'.",
        )
        self.assertEqual(
            self.module.build_slug("A___---...+++   ###B"),
            "a-b",
            "Missing edge case: collapse any mixed run of non-alphanumeric separators into a single '-'.",
        )
        self.assertEqual(
            self.module.build_slug("---___...+++   ###"),
            "",
            "Missing edge case: return an empty slug when input is only mixed non-alphanumeric separators.",
        )

    def test_build_slug_type_error(self):
        with self.assertRaisesRegex(
            TypeError,
            "title must be a string",
            msg="Missing edge case: reject non-string input with a clear TypeError.",
        ):
            self.module.build_slug(None)


if __name__ == "__main__":
    unittest.main()
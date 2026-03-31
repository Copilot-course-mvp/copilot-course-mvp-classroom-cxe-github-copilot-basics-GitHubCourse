import unittest

from tests.helpers import load_module_from_step


class TestStep02(unittest.TestCase):
    def setUp(self):
        self.module = load_module_from_step("step-02-chat-explain-fix-generate")

    def test_parse_scoreboard(self):
        parsed = self.module.parse_scoreboard("alice:10,bob:9,alice:14")
        self.assertEqual(parsed, {"alice": 14, "bob": 9})

    def test_parse_scoreboard_with_invalid_entries(self):
        parsed = self.module.parse_scoreboard("alice:10,bad,bob: 9,alice:notanumber")
        self.assertEqual(parsed, {"alice": 10, "bob": 9})

    def test_top_player(self):
        self.assertEqual(self.module.top_player({"alice": 5, "bob": 7}), ("bob", 7))
        self.assertEqual(self.module.top_player({"anna": 7, "bob": 7}), ("anna", 7))
        self.assertIsNone(self.module.top_player({}))


if __name__ == "__main__":
    unittest.main()
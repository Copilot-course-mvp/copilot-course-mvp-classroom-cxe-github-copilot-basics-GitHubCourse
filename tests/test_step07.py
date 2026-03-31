import unittest

from tests.helpers import load_module_from_step


class TestStep07(unittest.TestCase):
    def setUp(self):
        self.module = load_module_from_step("step-07-debugging-assistance")

    def test_summary_normal(self):
        data = self.module.summarize_response_times([120, 80, 100])
        self.assertEqual(data, {"min": 80.0, "max": 120.0, "avg": 100.0})

    def test_ignores_negative_and_handles_empty(self):
        data = self.module.summarize_response_times([-1, -9])
        self.assertEqual(data, {"min": 0.0, "max": 0.0, "avg": 0.0})


if __name__ == "__main__":
    unittest.main()
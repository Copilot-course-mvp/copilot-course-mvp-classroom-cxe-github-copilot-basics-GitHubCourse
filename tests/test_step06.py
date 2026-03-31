import unittest

from tests.helpers import load_module_from_step


class TestStep06(unittest.TestCase):
    def setUp(self):
        self.module = load_module_from_step("step-06-code-translation")

    def test_group_by_domain(self):
        emails = [
            "A@Example.com",
            "b@example.com",
            "bad-email",
            "c@other.org",
            "d@OTHER.ORG ",
        ]
        self.assertEqual(self.module.group_by_domain(emails), {"example.com": 2, "other.org": 2})


if __name__ == "__main__":
    unittest.main()
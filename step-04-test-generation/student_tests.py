import unittest
import importlib.util
from pathlib import Path


def _load_exercise_module():
    module_path = Path(__file__).with_name("exercise.py")
    spec = importlib.util.spec_from_file_location("step04_exercise", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


exercise = _load_exercise_module()


class TestSanitizeTags(unittest.TestCase):
    def test_basic_lowercase_and_trim(self):
        """Test that tags are lowercased and trimmed."""
        self.assertEqual(exercise.sanitize_tags(["  Hello ", "WORLD"]), ["hello", "world"])

    def test_empty_tags_removed(self):
        """Test that empty tags are removed after cleanup."""
        self.assertEqual(exercise.sanitize_tags(["", "   ", "valid"]), ["valid"])

    def test_duplicate_tags_removed(self):
        """Test that duplicate tags are deduplicated preserving first-seen order."""
        self.assertEqual(exercise.sanitize_tags(["python", "Python", "PYTHON"]), ["python"])

    def test_punctuation_stripped(self):
        """Test that punctuation characters are removed from tags."""
        self.assertEqual(exercise.sanitize_tags(["c++", "node.js", "a!b@c"]), ["c", "nodejs", "abc"])

    def test_hyphens_preserved(self):
        """Test that hyphens are kept in tags."""
        self.assertEqual(exercise.sanitize_tags(["front-end", "back-end"]), ["front-end", "back-end"])

    def test_empty_list(self):
        """Test that an empty input list returns an empty result."""
        self.assertEqual(exercise.sanitize_tags([]), [])

    def test_all_invalid_become_empty(self):
        """Test tags that become empty after punctuation removal are discarded."""
        self.assertEqual(exercise.sanitize_tags(["!!!", "...", "@@@"]), [])

    def test_duplicate_after_normalization(self):
        """Test that tags that are duplicate only after normalization are deduplicated."""
        self.assertEqual(exercise.sanitize_tags(["Hello!", "hello"]), ["hello"])


if __name__ == "__main__":
    unittest.main()
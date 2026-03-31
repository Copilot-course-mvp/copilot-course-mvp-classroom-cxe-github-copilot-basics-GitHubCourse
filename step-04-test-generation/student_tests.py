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
    def test_add_cases_generated_with_copilot(self):
        self.assertTrue(callable(exercise.sanitize_tags))


if __name__ == "__main__":
    unittest.main()
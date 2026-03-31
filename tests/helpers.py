import importlib.util
from pathlib import Path


def load_module_from_step(step_folder: str):
    file_path = Path(__file__).resolve().parent.parent / step_folder / "exercise.py"
    spec = importlib.util.spec_from_file_location(step_folder.replace("-", "_"), file_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module
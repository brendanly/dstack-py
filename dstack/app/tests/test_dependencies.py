import os
import shutil
from pathlib import Path
from tempfile import gettempdir
from unittest import TestCase

from dstack.app import _get_deps, _undress
from dstack.app.dependencies import _stage_deps
from dstack.app.tests.test_package.mymodule import test_app


class TestDependencies(TestCase):
    @staticmethod
    def _get_temp_dir(path: str = "") -> Path:
        return Path(gettempdir()) / "test_deps" / path

    def setUp(self):
        temp_base = self._get_temp_dir()
        if temp_base.exists():
            shutil.rmtree(temp_base)

    def test_simple(self):
        func = _undress(test_app)
        deps = _get_deps(func)
        print(deps)
        stage_dir = self._get_temp_dir("stage1")
        print(stage_dir)
        _stage_deps(deps, stage_dir)
        self.tree_view(stage_dir)

    @staticmethod
    def tree_view(root: Path):
        def traverse(path: Path, indent: str = ""):
            for f in os.listdir(path):
                file = path / Path(f)
                print(f"{indent}|-{file.name}")
                if file.is_dir():
                    traverse(file, indent + "\t")

        print(f"/-{root.name}")
        traverse(root, "\t")
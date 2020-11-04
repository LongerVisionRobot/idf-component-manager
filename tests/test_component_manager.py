import os
import shutil
import tempfile
from io import open

from idf_component_manager.core import ComponentManager


def test_init_project():
    tempdir = tempfile.mkdtemp()
    try:
        manifest_path = os.path.join(tempdir, 'main', 'idf_component.yml')
        manager = ComponentManager(path=tempdir)

        manager.create_manifest({})

        with open(manifest_path, mode='r', encoding='utf-8') as file:
            assert file.readline().startswith('## IDF Component Manager')

    finally:
        shutil.rmtree(tempdir)

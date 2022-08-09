from pathlib import Path
from typing import Tuple

import pytest
from click.testing import CliRunner
from utils import list_of_filenames


@pytest.fixture(scope="function")
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture(scope="session")
def create_file_system(tmp_path_factory) -> Tuple[Path, Path]:
    """Creates a temporary file system with directories and files"""
    directory = tmp_path_factory.mktemp("tmp")
    filepath: Path = Path(".")
    for filename in list_of_filenames():
        filepath = directory / filename
        filepath.write_text("\n".join(list_of_filenames()))
    return directory, filepath

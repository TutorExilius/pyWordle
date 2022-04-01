import pytest
from pathlib import Path

from toml import TomlDecodeError

from pywordle.logic.helper import get_app_version

class TestHelperFunctions:
    def test_get_app_version(self):
        WORKIND_DIR = Path(__file__).parent / "test_files"
        app_version = get_app_version(WORKIND_DIR)
        assert app_version == "1.2.3"

        WORKIND_DIR = Path(__file__).parent / "corrupt_test_files"

        with pytest.raises((FileNotFoundError, IOError, TomlDecodeError, KeyError)):
            app_version = get_app_version(WORKIND_DIR)




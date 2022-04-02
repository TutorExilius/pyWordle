"""All tests for helper functions"""

from pathlib import Path

import pytest
from pywordle.logic.helper import get_app_major_version, get_app_version, upper
from toml import TomlDecodeError


class TestHelperFunctions:
    """Testclass for helper functions (helper.py)"""

    @pytest.mark.dependency()
    def test_get_app_version(self):
        WORKIND_DIR = Path(__file__).parent / "test_files"
        app_version = get_app_version(WORKIND_DIR)
        assert app_version == "1.2.3"

        WORKIND_DIR = Path(__file__).parent / "corrupt_test_files"

        with pytest.raises((FileNotFoundError, IOError, TomlDecodeError, KeyError)):
            app_version = get_app_version(WORKIND_DIR)

    @pytest.mark.dependency(depends=["TestHelperFunctions::test_get_app_version"])
    def test_get_app_major_version(self):
        WORKIND_DIR = Path(__file__).parent / "test_files"
        app_major_version = get_app_major_version(WORKIND_DIR)
        assert app_major_version == "1"

    def test_upper(self):
        expected_word = "SPAẞ"
        uppered_word = upper("spaß")
        assert uppered_word == expected_word

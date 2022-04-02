"""
Module with helper functions.
"""

from pathlib import Path

import toml


def get_app_version(working_dir: Path) -> str:
    """Extract and get the veriosn of the app from pyproject.toml.

    :param working_dir: Path of current working dir.
    :type: pathlib.Path
    :return: Version of the app.
    :rtype: str
    :raises ValueError
    """

    with open(working_dir / "pyproject.toml", encoding="utf8", mode="r") as file:
        pyproject_file = toml.load(file)

    app_version = pyproject_file["tool"]["poetry"]["version"]

    if not app_version:
        raise ValueError("Could not read version from pyproject.toml")

    return app_version


def get_app_major_version(working_dir: Path) -> str:
    """Get the major version part.

    :param working_dir: Path of current working dir.
    :type: pathlib.Path
    :return: Major version.
    :rtype: str
    """

    return get_app_version(working_dir).split(".")[0]


def upper(word: str) -> str:
    """Upper given word and replace 'ß' to 'ẞ' if exist.

    :param word: The word to upper.
    :return: The uppered word.
    :rtype: str
    """
    return word.replace("ß", "ẞ").upper()

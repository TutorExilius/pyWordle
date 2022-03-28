from pathlib import Path

import pywordle.globals as globals
import toml


def get_app_version() -> str:
    with open(
            Path(globals.WORKING_DIR) / "pyproject.toml", encoding="utf8", mode="r"
    ) as file:
        pyproject_file = toml.load(file)

    app_version = pyproject_file["tool"]["poetry"]["version"]

    if not app_version:
        raise ValueError("Could not read version from pyproject.toml")

    return app_version


def get_app_major_version() -> str:
    return get_app_version().split(".")[0]

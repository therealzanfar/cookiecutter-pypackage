"""Tests for the cookiecutter system."""

import datetime
import os
import shlex
import subprocess
from contextlib import contextmanager
from pathlib import Path
from typing import Generator

from cookiecutter.utils import rmtree


@contextmanager
def inside_dir(dirpath: Path) -> Generator:
    """
    Execute code from inside the given directory.

    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = Path.cwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs) -> Generator:
    """
    Delete the temporal directory that is created when executing the tests.

    :param cookies: pytest_cookies.Cookies,
        cookie to be baked and its temporal files will be removed.
    """
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        rmtree(str(result.project_path))


def run_inside_dir(command: str, dirpath: Path) -> None:
    """
    Run a command from inside a given directory, returning the exit status.

    :param command: Command that will be executed
    :param dirpath: String, path of the directory the command is being run.
    """
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def check_output_inside_dir(command: str, dirpath: Path) -> None:
    """Run a command from inside a given directory, returning the command output."""
    with inside_dir(dirpath):
        return subprocess.check_output(shlex.split(command))


def get_project_inner_path(result) -> Path:
    return result.project_path / result.project_path.name


def find_in_file(file: Path, needle: str) -> bool:
    with open(file, encoding="utf-8") as fh:
        haystack = fh.read()
    return needle in haystack


def test_bake_with_defaults(cookies) -> None:
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        for expected in [
            ".editorconfig",
            ".gitignore",
            "LICENSE",
            "pyproject.toml",
            "README.md",
        ]:
            assert expected in found_toplevel_files


def test_year_compute_in_license_file(cookies) -> None:
    with bake_in_temp_dir(cookies) as result:
        license_file_path = result.project_path / "LICENSE"
        now = datetime.datetime.now()  # noqa: DTZ005
        with license_file_path.open("r") as f:
            assert str(now.year) in f.read()


def test_bake_and_run_tests(cookies) -> None:
    with bake_in_temp_dir(cookies) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("poetry run pytest", str(result.project_path)) == 0


def test_bake_with_cli_and_run_tests(cookies) -> None:
    with bake_in_temp_dir(
        cookies,
        extra_context={"command_line_interface": "Click"},
    ) as result:
        assert result.project_path.is_dir()

        inner_dir = get_project_inner_path(result)
        inner_files = [f.name for f in inner_dir.iterdir()]
        assert "__main__.py" in inner_files

        assert run_inside_dir("poetry run pytest", str(result.project_path)) == 0


def test_bake_with_apostrophe_and_run_tests(cookies) -> None:
    """Ensure that a `full_name` with apostrophes does not break setup.py."""
    with bake_in_temp_dir(
        cookies,
        extra_context={"full_name": "O'connor"},
    ) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("poetry run pytest", str(result.project_path)) == 0


def test_bake_selecting_license(cookies) -> None:
    license_strings = {
        "GPL-3.0-or-later": "GNU GENERAL PUBLIC LICENSE",
        "BSD-3-Clause": "BSD 3-Clause License",
        "MIT": "MIT License",
        "Apache-2.0": "Licensed under the Apache License, Version 2.0",
    }
    for license, target_string in license_strings.items():  # noqa: A001
        with bake_in_temp_dir(
            cookies,
            extra_context={"license": license},
        ) as result:
            inner_dir = get_project_inner_path(result)

            assert find_in_file(
                result.project_path / "pyproject.toml",
                license,
            )
            assert find_in_file(inner_dir / "__init__.py", license)
            assert find_in_file(result.project_path / "LICENSE", target_string)

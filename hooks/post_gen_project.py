#! /usr/bin/env python3
from pathlib import Path
import subprocess
import sys


PROJECT_DIRECTORY = Path.cwd()


def remove_file(*filepaths: str):
    Path(PROJECT_DIRECTORY).joinpath(*filepaths).unlink()


run_cmd = lambda args: subprocess.run(
    args.split(), capture_output=True, check=True, text=True
)


def main() -> int:
    if "No CLI" == "{{ cookiecutter.command_line_interface }}":
        remove_file("{{ cookiecutter.project_slug }}", "__main__.py")
        remove_file(
            "{{ cookiecutter.project_slug }}",
            "tests",
            "test_cli.py",
        )

    if "Proprietary" == "{{ cookiecutter.license }}":
        remove_file("LICENSE")

    print("Building Python Environment")
    run_cmd("poetry install")
    run_cmd("poetry run python3 -m pip install --upgrade pip wheel setuptools")

    print("Initializing Git repository")
    run_cmd("git init")
    run_cmd("git remote add origin {{cookiecutter.git_url}}.git")

    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Post-bake customizations."""  # noqa: INP001

import subprocess
import sys
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def remove_file(*filepaths: str) -> None:  # noqa: D103
    Path(PROJECT_DIRECTORY).joinpath(*filepaths).unlink()


def run_cmd(args: str, show_output: bool = False) -> int:  # noqa: D103
    if not show_output:
        try:
            proc = subprocess.run(
                args.split(),
                capture_output=True,
                check=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            print(e.args)
            if e.stdout:
                print(e.stdout)
            if e.stderr:
                print(e.stderr)

            raise (e)

        print(proc.stdout)
        return proc.returncode

    try:
        p = subprocess.Popen(
            args.split(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        assert p.stdout is not None

        with p.stdout:
            for line in iter(p.stdout.readline, b""):
                print(line.decode(), end="")
        p.wait()  # wait for the subprocess to exit
    except subprocess.CalledProcessError as e:
        print(e.args)
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)

        raise (e)

    return p.returncode


def main() -> int:  # noqa: D103
    if "No CLI" == "{{ cookiecutter.command_line_interface }}":  # noqa: PLR0133
        remove_file("{{ cookiecutter.project_slug }}", "__main__.py")
        remove_file("{{ cookiecutter.project_slug }}", "cli.py")
        remove_file(
            "{{ cookiecutter.project_slug }}",
            "tests",
            "test_cli.py",
        )

    if "Proprietary" == "{{ cookiecutter.license }}":  # noqa: PLR0133
        remove_file("LICENSE")

    run_cmd("sh setup.sh", show_output=True)
    remove_file("setup.sh")

    # print("Building Python Environment")
    # run_cmd("poetry env use python{{cookiecutter.python_min_version}}")
    # run_cmd("poetry install --with=dev")
    # run_cmd("poetry run python3 -m pip install --upgrade pip wheel setuptools")

    # print("Initializing Git repository")
    # run_cmd("git init")
    # run_cmd("git remote add origin {{cookiecutter.git_url}}.git")

    return 0


if __name__ == "__main__":
    sys.exit(main())

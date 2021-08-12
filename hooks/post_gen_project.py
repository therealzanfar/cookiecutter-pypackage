#! /usr/bin/python3
import subprocess
import sys

run_cmd = lambda args: subprocess.run(
    args, capture_output=True, check=True, text=True
)


def main() -> int:
    print("Building Python Environment")
    run_cmd(["poetry", "install"])

    print("Initializing Git repository")
    run_cmd(["git", "init"])
    run_cmd(["git", "remote", "add", "origin", "{{cookiecutter.git_url}}.git"])

    return 0


if __name__ == "__main__":
    sys.exit(main())

#! /usr/bin/python3
import subprocess
import sys

run_cmd = lambda args: subprocess.run(
    args, capture_output=True, check=True, text=True
)


def main() -> int:
    print("Building development environment...")
    run_cmd(["./mkenv.sh"])

    print("Initializing Git repository")
    run_cmd(["git", "init"])
    run_cmd(["git", "remote", "add", "origin", "{{cookiecutter.git_url}}.git"])


if __name__ == "__main__":
    sys.exit(main())

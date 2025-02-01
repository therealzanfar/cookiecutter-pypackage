#! /usr/bin/env sh

echo "Building Python Environment";
uv python pin python{{cookiecutter.python_min_version}}
uv sync --all-extras
uv run python3 -m pip install --upgrade pip setuptools

echo "Initializing Git repository"
git init
git remote add origin {{cookiecutter.git_url}}.git

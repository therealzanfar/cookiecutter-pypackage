#! /usr/bin/env sh

echo "Building Python Environment";
poetry env use python{{cookiecutter.python_min_version}}
poetry install --with=dev
poetry run python3 -m pip install --upgrade pip setuptools

echo "Initializing Git repository"
git init
git remote add origin {{cookiecutter.git_url}}.git

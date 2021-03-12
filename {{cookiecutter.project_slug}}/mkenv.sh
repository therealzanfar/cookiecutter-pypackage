#!/bin/bash

VENV=".venv";
PYVER="python{{cookiecutter.python_min_version}}";

${PYVER} -m venv "${VENV}";
"${VENV}/bin/${PYVER}" -m pip install --upgrade pip wheel;
"${VENV}/bin/${PYVER}" -m pip install -r requirements.txt;

#!/bin/bash

VENV=".venv";
PYVER="python3";

${PYVER} -m venv "${VENV}";
"${VENV}/bin/${PYVER}" -m pip install --upgrade pip wheel;
"${VENV}/bin/${PYVER}" -m pip install -r requirements.txt;

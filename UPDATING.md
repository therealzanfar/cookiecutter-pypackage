# Updating this cookiecutter

## Python Versions

The list of available Python versions should be taken from all released and
supported version listed at https://www.python.org/downloads/. I.e.,
prerelease versions should be avoided.

Versions tend to sunset in October, so updates should be made at least yearly
shortly after that time.

The version list needs to be changed in the following files:

* `cookiecutter.json` in the "python_min_version" key.
* `tox.ini` in the "[tox].envlist" key
* `pyproject.toml` needs it's Python dependency set to at least the minimum
  available version

## Python Modules

Both this cookiecutter package, and the generated package, have module
dependencies that should have their versions updated regularly. Helpfully,
most dependencies are shared, so versions from one can be copied to the other.

### To update the cookiecutter package's dependencies:

Dependencies should be updated approximately every quarter. Combined with the
Python version updates, that works out to the beginning of February, May,
August, and November.

For each dependency in `pyproject.toml`, ask `poetry` to update the version
with `poetry add <package>@latest`.

Currently, that means:

    poetry add cookiecutter@latest

    poetry add -G dev mypy@latest pytest@latest pytest-cookies@latest \
      pytest-runner@latest rich@latest ruff@latest tox@latest click@latest

Then copy the `mypy`, `pytest`, `ruff`, and `tox` versions to the `{{cookiecutter.project_slug}}/pyproject.toml` dependency list.

Finally, the versions of `click` and `rich` need to be manually updated based
on the versions listed at:

* https://pypi.org/project/click/
* https://pypi.org/project/rich/
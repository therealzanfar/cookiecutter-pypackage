====================================
Python Package Cookiecutter Template
====================================

Cookiecutter_ template for a Python package.

* GitHub repo: https://gitlab.com/zanfar/cookiecutter-pypackage
* Free software: BSD license
* Forked from: https://github.com/audreyfeldroy/cookiecutter-pypackage

Features
--------

* Testing setup with ``pytest``
* Tox_ testing: Setup to easily test for Python 3.6, 3.7, 3.8, and 3.9
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet

::

    pip install --upgrade cookiecutter

Generate a Python package project

::

    cookiecutter gl:zanfar/cookiecutter-pypackage

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `audreyfeldroy/cookiecutter-pypackage`_: The parent project with some more
  advanced features and integrations.

* `Nekroze/cookiecutter-pypackage`_: A fork of this with a PyTest test runner,
  strict flake8 checking with Travis/Tox, and some docs and ``setup.py``
  differences.

* `tony/cookiecutter-pypackage-pythonic`_: Fork with py2.7+3.3 optimizations.
  Flask/Werkzeug-style test runner, ``_compat`` module and module/doc
  conventions. See ``README.rst`` or the `github comparison view`_ for
  exhaustive list of additions and modifications.

* `ardydedase/cookiecutter-pypackage`_: A fork with separate requirements
  files rather than a requirements list in the ``setup.py`` file.

* `lgiordani/cookiecutter-pypackage`_: A fork of Cookiecutter that uses Punch_
  instead of bump2version_ and with separate requirements files.

* `briggySmalls/cookiecutter-pypackage`_: A fork using Poetry_ for neat
  package management and deployment, with linting, formatting, no makefiles
  and more.

* `veit/cookiecutter-namespace-template`_: A cookiecutter template for python
  modules with a namespace

* `zillionare/cookiecutter-pypackage`_: A template containing Poetry_,
  Mkdocs_, Github CI and many more. It's a template and a package also (can be
  installed with `pip`)

* `waynerv/cookiecutter-pypackage`_: A fork using Poetry_, Mkdocs_,
  Pre-commit_, Black_ and Mypy_. Run test, staging and release workflows with
  GitHub Actions, automatically generate release notes from CHANGELOG.

* Also see the `network`_ and `family tree`_ for this repo. (If you find
  anything that should be listed here, please add it and send a pull request!)


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _Read the Docs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _bump2version: https://github.com/c4urself/bump2version
.. _Punch: https://github.com/lgiordani/punch
.. _Poetry: https://python-poetry.org/
.. _PyPi: https://pypi.python.org/pypi
.. _Mkdocs: https://pypi.org/project/mkdocs/
.. _Pre-commit: https://pre-commit.com/
.. _Black: https://black.readthedocs.io/en/stable/
.. _Mypy: https://mypy.readthedocs.io/en/stable/

.. _`audreyfeldroy/cookiecutter-pypackage`: https://github.com/audreyfeldroy/cookiecutter-pypackage
.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`tony/cookiecutter-pypackage-pythonic`: https://github.com/tony/cookiecutter-pypackage-pythonic
.. _`ardydedase/cookiecutter-pypackage`: https://github.com/ardydedase/cookiecutter-pypackage
.. _`lgiordani/cookiecutter-pypackage`: https://github.com/lgiordani/cookiecutter-pypackage
.. _`briggySmalls/cookiecutter-pypackage`: https://github.com/briggySmalls/cookiecutter-pypackage
.. _`veit/cookiecutter-namespace-template`: https://github.com/veit/cookiecutter-namespace-template
.. _`zillionare/cookiecutter-pypackage`: https://zillionare.github.io/cookiecutter-pypackage/
.. _`waynerv/cookiecutter-pypackage`: https://waynerv.github.io/cookiecutter-pypackage/
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage-pythonic/compare/audreyr:master...master
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members

from distutils.util import convert_path
from setuptools import setup, find_packages
import sys

with open(convert_path("README.md"), "r", encoding="utf-8") as desc_file:
    long_description = desc_file.read()

PYVER = (
    {{cookiecutter.python_min_version[0]}},
    {{cookiecutter.python_min_version[2:]}},
)
if sys.version_info < PYVER:
    sys.exit(
        "Sorry, Python version {{cookiecutter.python_min_version}} or greater is required"
    )

setup(
    name="{{cookiecutter.project_slug}}",
    version="{{cookiecutter.project_version}}",
    author="""{{cookiecutter.full_name}}""",
    author_email="{{cookiecutter.email}}",
    description="{{cookiecutter.project_short_description}}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="",
    url="{{cookiecutter.git_url}}",
    packages=find_packages(),
    license="GPLv3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: {{cookiecutter.python_min_version}}",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Typing :: Typed",
    ],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.__main__:main",
        ]
    },
    install_requires=[
        "click",
    ],
    setup_requires=["pytest-runner"],
    test_suite="pytest",
    tests_require=[
        "pytest",
    ],
)

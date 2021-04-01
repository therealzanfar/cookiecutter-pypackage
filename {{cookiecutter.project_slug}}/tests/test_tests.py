#!/usr/bin/env python{{ cookiecutter.python_min_version }}

"""Test `{{ cookiecutter.project_slug }}` package test setup."""

from click.testing import CliRunner

from {{ cookiecutter.project_slug }}.__main__ import main


def test_pytest_operation():
    assert True


def test_cli():
    """Test the Click CLI"""

    runner = CliRunner()
    result = runner.invoke(main)

    assert result.exit_code == 0

    help_result = runner.invoke(main, ["--help"])

    assert help_result.exit_code == 0
    assert "--help" in help_result.output
    assert "Show this message and exit." in help_result.output

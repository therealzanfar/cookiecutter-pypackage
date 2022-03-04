#!/usr/bin/env python3

# cSpell:words {{cookiecutter.project_slug}}

"""Test `{{ cookiecutter.project_slug }}` package CLI tests"""

{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner

from {{ cookiecutter.project_slug }}.__main__ import main

def test_cli_click():
    """Test the Click CLI"""

    runner = CliRunner()
    result = runner.invoke(main)

    assert result.exit_code == 0

    help_result = runner.invoke(main, ["--help"])

    assert help_result.exit_code == 0
    assert "--help" in help_result.output
    assert "Show this message and exit." in help_result.output
{%- endif %}

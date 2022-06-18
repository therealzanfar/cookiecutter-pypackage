#! /usr/bin/env python3

# cSpell:words {{cookiecutter.project_slug}}

"""Console script for {{cookiecutter.project_slug}}."""

import logging
import sys

import click
from rich.logging import RichHandler


CLICK_CONTEXT = {"help_option_names": ["-h", "--help"]}


def setup_logging(verbosity: int = 0):
    """Setup a root logger with console output

    Args:
        verbosity (int, optional): The logging level; 0=Error, 1=Warning,
            2=Info, 3+=Debug. Defaults to 0.
    """

    logging_level = logging.ERROR
    if verbosity == 1:
        logging_level = logging.WARNING
    elif verbosity == 2:
        logging_level = logging.INFO
    elif verbosity >= 3:
        logging_level = logging.DEBUG

    logging.basicConfig(
        level=logging_level,
        format="%(message)s",
        datefmt="[%x]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )


@click.command(context_settings=CLICK_CONTEXT)
@click.option("-v", "--verbose", count=True)
def cli(verbose: int = 0) -> int:
    """Main entry point for {{cookiecutter.project_slug}}"""

    args = locals().items()
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    logger.debug(
        "Running with options: %s",
        ", ".join(f'{k!s}={v!r}' for k,v in args)
    )

    return 0


if __name__ == "__main__":
    sys.exit(cli())

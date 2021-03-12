#! /usr/bin/python3
import logging
import sys

from typing import Any, Optional, Union
from typing import Sequence, List, Tuple, Mapping, Dict
from typing import TypedDict, NewType, TypeVar, cast

import click

"""Console script for {{cookiecutter.project_slug}}."""


CLICK_CONTEXT = {"help_option_names": ["-h", "--help"]}


def setup_logging(verbosity: int = 0):
    """Setup a root logger with console output

    Args:
        verbosity (int, optional): The logging level; 0=Error, 1=Warning, 2=Info, 3+=Debug. Defaults to 0.
    """

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    logger = logging.getLogger(__name__)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.CRITICAL)
    console_handler.setFormatter(
        logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
    )

    if not verbosity or verbosity == 0:
        console_handler.setLevel("ERROR")
    elif verbosity == 1:
        console_handler.setLevel("WARNING")
    elif verbosity == 2:
        console_handler.setLevel("INFO")
    elif verbosity >= 3:
        console_handler.setLevel("DEBUG")
    else:
        logger.critical("Unexplained negative count while setting handler verbosity")

    root_logger.addHandler(console_handler)


@click.command(context_settings=CLICK_CONTEXT)
@click.option("-v", "--verbose", count=True)
def main(verbose: int) -> int:
    """Main entry point for {{cookiecutter.project_slug}}"""

    vars = locals().items()
    setup_logging(verbose)
    logger = logging.getLogger(__name__)
    logger.debug(f"Running with options: {', '.join(f'{k}={v!r}' for k,v in vars)}")

    return 0

if __name__ == "__main__":
    sys.exit(main())

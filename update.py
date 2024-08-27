#!/usr/bin/env python3

"""Update this cookiecutter package and it's templates."""

import logging
import re
import subprocess
from enum import Enum, auto
from typing import Iterable, NamedTuple

from rich.logging import RichHandler


class Dependency(NamedTuple):
    """Details about a pyproject dependency."""

    module: str
    version: str
    group: str


CLICK_CONTEXT = {"help_option_names": ["-h", "--help"]}


EXCLUDED_DEPENDENCIES = [
    "python",
]

RE_DEP_HEADER_GROUP = re.compile(
    r"^\[tool\.poetry\.group\.(?P<group>[a-z]+)\.dependencies\]$",
    flags=re.I,
)
RE_DEP_HEADER = re.compile(
    r"^\[tool\.poetry\.dependencies\]$",
    flags=re.I,
)
RE_DEP_SPEC = re.compile(
    r'^(?P<module>[a-z]+) = "\^(?P<version>[0-9\.]+)"$',
    flags=re.I,
)


class ParseState(Enum):
    """TOML Parsing State."""

    IDLE = auto()
    DEPS = auto()




def setup_logging(verbosity: int = 0, force: bool = False) -> None:
    """
    Set up a root logger with console output.

    Args:
        verbosity (int, optional): The logging level; 0=Error, 1=Warning,
            2=Info, 3+=Debug. Defaults to 0.

        force (bool, optional): Force the logging level to this value, even
            if it's currently set to a more permissive value.",

    """
    logging_level = logging.ERROR
    if verbosity == 1:
        logging_level = logging.WARNING
    elif verbosity == 2:  # noqa: PLR2004
        logging_level = logging.INFO
    elif verbosity >= 3:  # noqa: PLR2004
        logging_level = logging.DEBUG

    if len(logging.root.handlers) == 0:
        logging.basicConfig(
            level=logging_level,
            format="%(message)s",
            datefmt="[%x]",
            handlers=[RichHandler(rich_tracebacks=True)],
        )
        logger = logging.getLogger(__name__)
        logger.info(f"Logging Setup at {logging.getLevelName(logging_level)} level")

    elif logging.root.level > logging_level or force:
        logging.root.setLevel(logging_level)

        logger = logging.getLogger(__name__)
        logger.info(f"Logging updated to {logging.getLevelName(logging_level)} level")

    else:
        logger = logging.getLogger(__name__)
        logger.debug(
            "Ignoring logging setup request: "
            "handler already exists at desired or greater level",
        )

def extract_pyproject_dependencies(path: str) -> Iterable[Dependency]:
    """
    Find and return all dependencies listed in a pyproject.toml file.

    This is a brute-force solution instead of being based on a TOML library
    so that it works on Jinja templates as well.
    """
    with open(path, encoding="utf-8") as fh:
        state = ParseState.IDLE
        group = ""

        for line in fh:
            # print(line.rstrip())

            if state is ParseState.IDLE:
                if m := RE_DEP_HEADER_GROUP.match(line):
                    state = ParseState.DEPS
                    group = m.group("group")

                    # print(f"Found dependency group: {line.rstrip()}")

                    continue

                if m := RE_DEP_HEADER.match(line):
                    state = ParseState.DEPS
                    group = ""

                    # print(f"Found dependency group: {line.rstrip()}")

                    continue

            if state is ParseState.DEPS:
                if m := RE_DEP_SPEC.match(line):
                    module=m.group("module")
                    version=m.group("version")

                    yield Dependency(
                        module=module,
                        version=version,
                        group=group,
                    )

                    continue

                if len(line.strip()) <= 0:
                    state = ParseState.IDLE


def update_pyproject_dependencies(path: str, versions: dict[str, str]) -> None:
    """
    Find and update all dependencies listed in a pyproject.toml file.

    This is a brute-force solution instead of being based on a TOML library
    so that it works on Jinja templates as well.
    """
    with open(path, encoding="utf-8") as fh:
        original = fh.readlines()

    with open(path, mode="w", encoding="utf-8") as fh:
        state = ParseState.IDLE

        for line in original:
            # print(line.rstrip())

            if state is ParseState.IDLE:
                if (m := RE_DEP_HEADER_GROUP.match(line)) or \
                        (m := RE_DEP_HEADER.match(line)):
                    state = ParseState.DEPS
                    # print(f"Found dependency group: {line.rstrip()}")
                    fh.write(line)

                else:
                    fh.write(line)

            elif state is ParseState.DEPS:
                if m := RE_DEP_SPEC.match(line):
                    module = m.group("module")

                    if module in versions:
                        fh.write(f'{module} = "^{versions[module]}"\n')

                    else:
                        fh.write(line)

                elif len(line.strip()) <= 0:
                    state = ParseState.IDLE
                    fh.write(line)

                else:
                    fh.write(line)


def get_latest_package_version(module: str) -> str:
    """Query PIP for the latest version available."""
    ps = subprocess.run(
        ["pip", "index", "versions", module],
        text=True,
        capture_output=True,
        check=True,
    )

    for line in ps.stdout.splitlines():

        if line.startswith("Available versions: "):
            versions = re.split(r",?\s+", line)

            # print(line.rstrip())
            # print(versions)

            if len(versions) >= 3:  # noqa: PLR2004
                return versions[2]

    raise ValueError(f"No versions found for {module}")

if __name__ == "__main__":
    sources = [
        "pyproject.toml",
        "{{cookiecutter.project_slug}}/pyproject.toml",
    ]
    versions = {}

    setup_logging()

    for src in sources:
        print(f"Scraping {src} for dependencies...")
        for dep in extract_pyproject_dependencies(src):
            if dep.module not in EXCLUDED_DEPENDENCIES:
                versions[dep.module] = dep.version


                if dep.group == "":
                    print(f"+ Found dependency '{dep.module}' at version {dep.version}")
                else:
                    print(
                        f"+ Found {dep.group} dependency "
                        f"'{dep.module}' at version {dep.version}",
                    )

    print()

    for module in versions:
        v = get_latest_package_version(module)
        versions[module] = v
        print(f"Latest version of {module} is {v}")
    print()

    for src in sources:
        print(f"Updating {src} dependencies...")
        update_pyproject_dependencies(src, versions)
    print()

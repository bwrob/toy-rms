"""Utility functions for naming conventions."""

import re

PATTERN = re.compile(
    r"""
        (?<=[a-z])      # preceded by lowercase
        (?=[A-Z])       # followed by uppercase
        |               # OR
        (?<=[A-Z])      # preceded by lowercase
        (?=[A-Z][a-z])  # followed by uppercase, then lowercase
    """,
    re.VERBOSE,
)


def to_snake_case(name: str) -> str:
    """Convert a string to snake_case."""
    return PATTERN.sub("_", name).lower()

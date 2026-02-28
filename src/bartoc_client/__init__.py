"""A client to BARTOC."""

from .api import hello, square

# being explicit about exports is important!
__all__ = [
    "hello",
    "square",
]

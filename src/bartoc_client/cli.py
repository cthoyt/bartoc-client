"""Command line interface for :mod:`bartoc_client`."""

import click

__all__ = [
    "main",
]


@click.command()
def main() -> None:
    """CLI for bartoc_client."""


if __name__ == "__main__":
    main()

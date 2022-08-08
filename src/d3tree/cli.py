from os import getcwd

import click

from d3tree import utils


@click.command()
@click.argument("path", default=getcwd())
def main(path: str):
    filepath_iter = utils.generator_from_path(path=path)
    utils.print_iterator(iter_=filepath_iter)


if __name__ == "__main__":
    main()

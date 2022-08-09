import os
import sys
from typing import Optional, TextIO, Union

import click

from d3tree import utils


@click.command()
@click.argument("path", type=click.Path(exists=True, file_okay=True, dir_okay=True), required=False)
def main(path: Optional[Union[str, TextIO]]) -> None:
    if path and isinstance(path, str):
        iter_ = utils.generator_from_path(path=path)
        utils.print_iterator(iter_=iter_)
        return
    elif click.get_text_stream("stdin"):
        path = sys.stdin
    else:
        path = os.getcwd()
    for line in path:
        print(line)


if __name__ == "__main__":
    main()

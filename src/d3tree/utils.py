from os import scandir
from typing import Generator, Iterator


def generator_from_path(path: str, max_depth: int = 1, cur_depth: int = 1) -> Generator:
    """Retrieves files and directories from path recursively, up to max depth"""
    for entry in scandir(path):
        if entry.is_dir() and cur_depth < max_depth:
            yield from generator_from_path(entry.path, max_depth=max_depth, cur_depth=cur_depth + 1)
        elif entry.is_file():
            yield entry


def print_iterator(iter_: Iterator) -> None:
    """Prints the elements of the provided iterator"""
    try:
        while True:
            file = next(iter_)
            print(file.name)
    except StopIteration:
        pass

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/d3tree) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/d3tree) ![PyPI](https://img.shields.io/pypi/v/d3tree) [![GitHub license](https://img.shields.io/github/license/dkreeft/d3tree)](https://github.com/dkreeft/d3tree/blob/main/LICENSE) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/dkreeft/d3tree) [![GitHub issues](https://img.shields.io/github/issues/dkreeft/d3tree)](https://github.com/dkreeft/d3tree/issues) [![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fdkreeft%2Fd3tree)](https://twitter.com/intent/tweet?text=Cool%020Python%020package:&url=https%3A%2F%2Fgithub.com%2Fdkreeft%2Fd3tree)

# d3tree

`d3tree` is a Python package used to visualize file paths using D3.js. The package is inspired by [Dirtree](https://github.com/emad-elsaid/dirtree), a similar library written in Ruby.

## Installation

Install `d3tree` in your virtual environment of choice using:

```shell
python -m pip install d3tree
```

## Usage

`d3tree` is a command-line utility that can be used as follows:

```shell
Usage: d3tree [OPTIONS] [PATH]

Options:
  -v, --version                   Print version
  -o, --output TEXT               Specify filepath to write HTML output
  -t, --template [tree|circles|flame|treemap]
                                  Specify template
  --help                          Show this message and exit.
```

### Examples

Visualize current directory:

```shell
ls | d3tree -o output.html
```

Or use a file that contains the filepaths:

```shell
cat filepaths.txt | d3tree -o output.html
```

## Features not implemented

The following features are not implemented (yet):
- shell completion
- screenshot feature
- using local JS dependencies

Feel free to create a PR for these or other features.

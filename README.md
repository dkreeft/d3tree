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
d3tree -o output.html **/* *
```

## Features not implemented

The following features are not implemented (yet):
- shell completion
- screenshot feature
- using local dependencies

Feel free to create a PR for these or other features.

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
d3tree [OPTIONS] [PATH]

Options:
-v, --version      Prints version
-h, --help         Prints this help text
-o, --output       Specifies a path and filename to write HTML output
-t, --template     Specifies the template to use. Available options are "circles", "flame", "tree", "treemap"
```

### Examples

Visualize current directory:

```shell
d3tree -o output.html **/* *
```
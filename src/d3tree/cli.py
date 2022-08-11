from typing import Optional, TextIO, Union

import click

from d3tree import node, template, utils


def read_file(filepath: str, node: node.Node):
    with open(file=filepath, mode="r") as f:
        lines = filter(None, (line.strip() for line in f))
        for line in lines:
            node.insert_node(path=line.split("/"))


@click.command()
@click.argument("path", type=click.Path(exists=True, file_okay=True, dir_okay=True), required=False)
def main(path: Optional[Union[str, TextIO]]) -> None:
    if path and isinstance(path, str):
        iter_ = utils.generator_from_path(path=path)
    elif click.get_text_stream("stdin"):
        iter_ = utils.read_from_stdin()
    else:
        return None

    # utils.print_iterator(iter_=iter_)
    data = utils.create_node(iter_=iter_)
    content = template.process_html(template="output", output="test", data=data)
    if content is not None:
        click.echo(content)


if __name__ == "__main__":
    main()

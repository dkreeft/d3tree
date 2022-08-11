from string import Template
from typing import Literal, Optional

from d3tree import node


class HtmlTemplate(Template):
    delimiter = "{%"  # to be replaced in HTML template


def read_html_template(template: str) -> str:
    with open(file=f"templates/{template}.html", mode="r") as html_file:
        content = html_file.read()

    return content


def write_html_file(name: str, content: str) -> None:
    with open(file=f"output/{name}.html", mode="w") as target:
        target.write(content)


def process_html(data: node.Node, template: Literal["tree", "output"], output: Optional[str] = None) -> Optional[str]:
    html_file = read_html_template(template=template)

    s = HtmlTemplate(html_file)
    content = s.substitute(data=data)

    if output:
        write_html_file(name=output, content=content)
        return None

    return content

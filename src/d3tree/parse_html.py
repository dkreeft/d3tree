from string import Template
from typing import Literal


class HtmlTemplate(Template):
    delimiter = "{%"


def read_html_template(template: str) -> str:
    with open(file=f"templates/{template}.html", mode="r") as html_file:
        content = html_file.read()

    return content


def write_html_file(name: str, content: str) -> None:
    with open(file=f"output/{name}.html", mode="w") as target:
        target.write(content)


def process_html(template: Literal["tree", "output"], output: str) -> None:
    data = {"name": "/", "children": [{"name": "child", "children": []}]}

    html_file = read_html_template(template=template)

    s = HtmlTemplate(html_file)
    content = s.substitute(data=data)

    write_html_file(name=output, content=content)


if __name__ == "__main__":
    process_html(template="output", output="test")

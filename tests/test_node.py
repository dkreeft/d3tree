from d3tree.node import Node


def test_node_output(create_file_system):
    root = Node(name="/")
    with open(file=create_file_system[1], mode="r") as f:
        lines = filter(None, (line.strip() for line in f))
        for line in lines:
            root.insert_node(path=line.split("/"))
    exp = (
        '{"name":"/","children":[{"name":"file_a.txt","children":[]},{"name":"file_b.txt","children":[]},'
        '{"name":"another_file.txt","children":[]}]}'
    )
    assert f"{root}" == exp


def test_no_children_node_output():
    root = Node(name="/")
    exp = '{"name":"/","children":[]}'
    assert f"{root}" == exp


def test_empty_node_output():
    root = Node(name="")
    exp = '{"name":"","children":[]}'
    assert f"{root}" == exp

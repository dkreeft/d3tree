import os

import pkg_resources
import pytest

import d3tree.cli as d3


@pytest.mark.parametrize("args", [("-v"), ("--version")])
def test_main_version(runner, args):
    result = runner.invoke(cli=d3.main, args=[args])
    output = result.output.strip()
    exp = pkg_resources.require("d3tree")[0].version
    assert result.exit_code == 0
    assert output == exp


@pytest.mark.parametrize("args, fn", [("-o", "output1.html"), ("--output=", "output2.html")])
def test_main_output(runner, create_file_system, args, fn):
    filepath = create_file_system[0] / fn
    result = runner.invoke(cli=d3.main, args=[f"{args}{filepath}"])
    assert result.exit_code == 0
    assert os.path.isfile(filepath)


@pytest.mark.parametrize("args, fn", [("-o", ""), ("--output=", "")])
def test_main_output_no_filename(runner, create_file_system, args, fn):
    filepath = create_file_system[0] / fn
    result = runner.invoke(cli=d3.main, args=[f"{args}{filepath}"])
    assert result.exit_code == 1
    assert not os.path.isfile(filepath)


@pytest.mark.parametrize("template", [("tree"), ("circles"), ("flame"), ("treemap")])
@pytest.mark.parametrize("args", [("-t"), ("--template=")])
def test_main_template(runner, args, template):
    result = runner.invoke(cli=d3.main, args=[f"{args}{template}"])
    assert result.exit_code == 0
    assert result.output


@pytest.mark.parametrize("template", [("tree"), ("circles"), ("flame"), ("treemap")])
@pytest.mark.parametrize("t_args", [("-t"), ("--template=")])
@pytest.mark.parametrize("o_args", [("-o"), ("--output=")])
def test_main_template_output(runner, create_file_system, t_args, o_args, template):
    filepath = create_file_system[0] / template
    result = runner.invoke(cli=d3.main, args=[f"{t_args}{template}", f"{o_args}{filepath}"])
    assert result.exit_code == 0
    assert not result.output
    assert os.path.isfile(filepath)
    os.remove(filepath)

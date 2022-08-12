import os
import subprocess

import pkg_resources
import pytest
from utils import list_of_filenames

import d3tree.cli as d3


@pytest.mark.xfail(reason="behavior has changed")
def test_main_without_path(runner, create_file_system):
    result = runner.invoke(cli=d3.main)
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert len(output) == 0


@pytest.mark.xfail(reason="behavior has changed")
def test_main_with_path(runner, create_file_system):
    result = runner.invoke(cli=d3.main, args=[f"{create_file_system[0]}"])
    output = result.output.splitlines()
    assert result.exit_code == 0
    assert sorted(output) == sorted(list_of_filenames())


@pytest.mark.xfail(reason="behavior has changed")
def test_main_pipeline(create_file_system):
    result = subprocess.check_output([f"cat {create_file_system[1]} | d3tree"], shell=True)
    decoded_result = result.decode(encoding="UTF-8")
    filtered_result = filter(None, decoded_result.split(sep="\n"))
    assert sorted(filtered_result) == sorted(list_of_filenames())


@pytest.mark.xfail(reason="behavior has changed")
def test_main_redirection(create_file_system):
    result = subprocess.check_output([f"d3tree < {create_file_system[1]}"], shell=True)
    decoded_result = result.decode(encoding="UTF-8")
    filtered_result = filter(None, decoded_result.split(sep="\n"))
    assert sorted(filtered_result) == sorted(list_of_filenames())


@pytest.mark.xfail(reason="behavior has changed")
def test_main_with_path_and_pipe(create_file_system):
    result = subprocess.check_output([f"echo 'foo/bar.txt' | d3tree {create_file_system[0]}"], shell=True)
    decoded_result = result.decode(encoding="UTF-8")
    filtered_result = filter(None, decoded_result.split(sep="\n"))
    assert sorted(filtered_result) == sorted(list_of_filenames())


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

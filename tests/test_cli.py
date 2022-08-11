import subprocess

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
def test_main_pipeline(runner, create_file_system):
    result = subprocess.check_output([f"cat {create_file_system[1]} | d3tree"], shell=True)
    decoded_result = result.decode(encoding="UTF-8")
    filtered_result = filter(None, decoded_result.split(sep="\n"))
    assert sorted(filtered_result) == sorted(list_of_filenames())


@pytest.mark.xfail(reason="behavior has changed")
def test_main_redirection(runner, create_file_system):
    result = subprocess.check_output([f"d3tree < {create_file_system[1]}"], shell=True)
    decoded_result = result.decode(encoding="UTF-8")
    filtered_result = filter(None, decoded_result.split(sep="\n"))
    assert sorted(filtered_result) == sorted(list_of_filenames())


@pytest.mark.xfail(reason="behavior has changed")
def test_main_with_path_and_pipe(runner, create_file_system):
    result = subprocess.check_output([f"echo 'foo/bar.txt' | d3tree {create_file_system[0]}"], shell=True)
    decoded_result = result.decode(encoding="UTF-8")
    filtered_result = filter(None, decoded_result.split(sep="\n"))
    assert sorted(filtered_result) == sorted(list_of_filenames())

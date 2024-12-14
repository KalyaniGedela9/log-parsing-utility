import subprocess
import pytest
from pathlib import Path

@pytest.fixture
def run_command():
    """Fixture to run commands from util.py with dynamic arguments."""
    def _run_command(arguments):
        result = subprocess.run(
            ["python", "util.py"] + arguments,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout, result.stderr

    return _run_command

def test_first_lines(run_command):
    """Test for the '--first' option to retrieve the first n lines."""
    stdout, stderr = run_command(["--first", "3", "Sample.log"])
    assert "Error" not in stderr
    assert len(stdout.splitlines()) <= 5

def test_last_lines(run_command):
    """Test for the '--last' option to retrieve the last n lines."""
    stdout, stderr = run_command(["--last", "3", "Sample.log"])
    assert "Error" not in stderr
    assert len(stdout.splitlines()) <= 5

def test_timestamps(run_command):
    """Test for the '--timestamps' option to ensure correct timestamp format."""
    stdout, stderr = run_command(["--timestamps", "Sample.log"])
    assert "Error" not in stderr
    assert any(line.startswith("2024-12-14") for line in stdout.splitlines())

def test_ipv4(run_command):
    """Test for the '--ipv4' option to match IPv4 addresses."""
    stdout, stderr = run_command(["--ipv4", "Sample.log"])
    assert "Error" not in stderr
    assert any("192.168." in line for line in stdout.splitlines())

def test_ipv6(run_command):
    """Test for the '--ipv6' option to match IPv6 addresses."""
    stdout, stderr = run_command(["--ipv6", "Sample.log"])
    assert "Error" not in stderr
    assert any("2001:" in line for line in stdout.splitlines())

def test_combined_options(run_command):
    """Test for combined options, ensuring correct handling of multiple flags."""
    stdout, stderr = run_command(["--ipv4", "--last", "3", "Sample.log"])
    assert "Error" not in stderr
    assert len(stdout.splitlines()) <= 10

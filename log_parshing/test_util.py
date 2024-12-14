import subprocess
import pytest
from pathlib import Path

@pytest.fixture
def run_command():
    """Helper function to run util.py commands dynamically with provided arguments."""
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
    """Test the --first option."""
    stdout, stderr = run_command(["--first", "3", "Sample.log"])
    assert "Error" not in stderr
    assert len(stdout.splitlines()) <= 5

def test_last_lines(run_command):
    """Test the --last option."""
    stdout, stderr = run_command(["--last", "3", "Sample.log"])
    assert "Error" not in stderr
    assert len(stdout.splitlines()) <= 5

def test_timestamps(run_command):
    """Test the --timestamps option."""
    stdout, stderr = run_command(["--timestamps", "Sample.log"])
    print("STDOUT:", stdout)  # Debugging
    assert "Error" not in stderr
    assert any(line.startswith("2024-12-14") for line in stdout.splitlines())  # Match date format

def test_ipv4(run_command):
    """Test the --ipv4 option."""
    stdout, stderr = run_command(["--ipv4", "Sample.log"])
    print("STDOUT:", stdout)  # Debugging
    assert "Error" not in stderr
    assert any("192.168." in line for line in stdout.splitlines())  # Match IPv4

def test_ipv6(run_command):
    """Test the --ipv6 option."""
    stdout, stderr = run_command(["--ipv6", "Sample.log"])
    print("STDOUT:", stdout)  # Debugging
    assert "Error" not in stderr
    assert any("2001:" in line for line in stdout.splitlines())  # Match IPv6


def test_combined_options(run_command):
    """Test a combination of options."""
    stdout, stderr = run_command(["--ipv4", "--last", "3", "Sample.log"])
    assert "Error" not in stderr
    assert len(stdout.splitlines()) <= 10

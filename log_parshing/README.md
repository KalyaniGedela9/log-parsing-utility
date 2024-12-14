Log Parsing Utility

Overview

This Log Parsing Utility is a Python-based command-line tool designed to analyze and filter log files effectively. It provides various options for extracting information such as timestamps, IPv4 and IPv6 addresses, and specific lines from the log files. The tool is complemented with a robust test suite to ensure functionality and reliability.

Features

Extract and display lines containing:

Timestamps in HH:MM:SS format

IPv4 addresses

IPv6 addresses

Display the first or last N lines from the log file

Modular design for easy integration and extension

Prerequisites

Python 3.8 or above

Setup and Installation

Clone the repository:

git clone <repository-url>
cd log_parshing-utility

Create a virtual environment:

python -m venv log_parshing
source log_parshing/bin/activate  # On Windows: log_parshing\Scripts\activate

Install the required dependencies:

pip install -r requirements.txt

Ensure the following directory structure:

log_parshing-utility/
|-- log_parshing/
    |-- util.py
    |-- test_util.py
    |-- Sample.log
    |-- requirements.txt

Usage

Run the utility with the desired options:

python util.py [OPTIONS] Sample.log

Command-line Options:

--first NUM     : Display the first NUM lines from the log file.

--last NUM      : Display the last NUM lines from the log file.

--timestamps    : Display lines containing timestamps in HH:MM:SS format.

--ipv4          : Display lines containing IPv4 addresses.

--ipv6          : Display lines containing IPv6 addresses.

Examples:

Display the first 5 lines of the log file:

python util.py --first 5 Sample.log

Extract lines with IPv4 addresses:

python util.py --ipv4 Sample.log

Extract lines containing timestamps:

python util.py --timestamps Sample.log

Testing

Automated tests are provided using pytest. To execute the tests:

pytest -s test_util.py

Sample Test Output

Sample outputs for various test cases are included in the test_util.py script. Below is an example test case:

Testing the --ipv4 option:

python util.py --ipv4 Sample.log

Expected Output:

2024-12-14 10:20:00 - INFO - User login attempt - IP: 192.168.1.1
2024-12-14 10:21:05 - ERROR - Invalid login attempt - IP: 192.168.1.2

File Descriptions

util.py

The main script for parsing log files with flexible options to filter data based on user input.

test_util.py

Comprehensive test suite to validate the functionality of util.py using pytest.

Sample.log

A sample log file for testing and demonstration purposes.

requirements.txt

Contains the Python dependencies required for the project.

Notes

Ensure the virtual environment is activated when running the utility or tests.

If modifying the requirements.txt file, include only the explicitly installed dependencies to avoid bloating.
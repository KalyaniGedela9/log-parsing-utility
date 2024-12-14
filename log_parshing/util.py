"""
Log Parsing Utility
-------------------
This script provides a command-line interface (CLI) for parsing log files. 
It supports filtering logs based on various criteria such as timestamps, 
IPv4 and IPv6 addresses, and line numbers.

Usage:
    ./util.py [OPTION]... [FILE]
    For detailed usage, run: ./util.py -h
"""

import argparse
import re
import sys

def contains_ipv4(line):
    """
    Checks if a line contains a valid IPv4 address.

    Args:
        line (str): The line to check.

    Returns:
        Match object if an IPv4 address is found, else None.
    """
    ipv4_pattern = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    return re.search(ipv4_pattern, line)

def contains_ipv6(line):
    """
    Checks if a line contains a valid IPv6 address in standard notation.

    Args:
        line (str): The line to check.

    Returns:
        Match object if an IPv6 address is found, else None.
    """
    ipv6_pattern = r'([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'
    return re.search(ipv6_pattern, line)

def contains_timestamp(line):
    """
    Checks if a line contains a timestamp in HH:MM:SS format.

    Args:
        line (str): The line to check.

    Returns:
        Match object if a timestamp is found, else None.
    """
    timestamp_pattern = r'\b([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])\b'
    return re.search(timestamp_pattern, line)

def get_first_n_lines(lines, num):
    """
    Retrieves the first `num` lines from a list of lines.

    Args:
        lines (list): The list of log lines.
        num (int): Number of lines to retrieve.

    Returns:
        list: The first `num` lines.
    """
    return lines[:num]

def get_last_n_lines(lines, num):
    """
    Retrieves the last `num` lines from a list of lines.

    Args:
        lines (list): The list of log lines.
        num (int): Number of lines to retrieve.

    Returns:
        list: The last `num` lines.
    """
    return lines[-num:]



def main():
    """
    Main entry point for the Log Parsing Utility.
    Parses command-line arguments, applies filters, and prints matching results.
    """
    parser = argparse.ArgumentParser(description="Log Parsing Utility")
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Log file to parse (or stdin)')
    parser.add_argument('-f', '--first', type=int, help='Print the first NUM lines')
    parser.add_argument('-l', '--last', type=int, help='Print the last NUM lines')
    parser.add_argument('-t', '--timestamps', action='store_true', help='Print lines containing a timestamp')
    parser.add_argument('-i', '--ipv4', action='store_true', help='Print lines containing an IPv4 address')
    parser.add_argument('-I', '--ipv6', action='store_true', help='Print lines containing an IPv6 address')

    args = parser.parse_args()

    if args.first and args.last:
        print("Error: --first and --last options cannot be used together.")
        sys.exit(1)

    if not any([args.first, args.last, args.ipv4, args.ipv6, args.timestamps]):
        print("Error: No valid options provided. Use -h for help.")
        sys.exit(1)

    lines = args.file.readlines()
    if not lines:
        print("No input provided. Please provide a log file or use standard input.")
        sys.exit(1)

    if args.first:
        lines = get_first_n_lines(lines, args.first)
    if args.last:
        lines = get_last_n_lines(lines, args.last)
    if args.ipv4:
        lines = [line for line in lines if contains_ipv4(line)]
    if args.ipv6:
        lines = [line for line in lines if contains_ipv6(line)]
    if args.timestamps:
        lines = [line for line in lines if contains_timestamp(line)]

    if lines:
        print("\n".join(line.strip() for line in lines))
    else:
        print("No matching results found.")

if __name__ == "__main__":
    main()

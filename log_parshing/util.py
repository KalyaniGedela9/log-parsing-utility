import argparse
import re
import sys

# Function to check if a string contains a valid IPv4 address
def contains_ipv4(line):
    ipv4_pattern = r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    return re.search(ipv4_pattern, line)

# Function to check if a string contains a valid IPv6 address
def contains_ipv6(line):
    ipv6_pattern = r'([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'
    return re.search(ipv6_pattern, line)

# Function to check if a string contains a timestamp in HH:MM:SS format
def contains_timestamp(line):
    timestamp_pattern = r'\b([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])\b'
    return re.search(timestamp_pattern, line)

# Function to get the first N lines from a list of lines
def get_first_n_lines(lines, num):
    return lines[:num]

# Function to get the last N lines from a list of lines
def get_last_n_lines(lines, num):
    return lines[-num:]

# Function to filter lines containing IPv4 addresses
def filter_ipv4_lines(lines):
    return [line for line in lines if contains_ipv4(line)]

# Function to filter lines containing IPv6 addresses
def filter_ipv6_lines(lines):
    return [line for line in lines if contains_ipv6(line)]

# Function to filter lines containing timestamps
def filter_timestamp_lines(lines):
    return [line for line in lines if contains_timestamp(line)]

# Function to parse command-line arguments and handle file operations
def main():
    parser = argparse.ArgumentParser(description="Log Parsing Utility")
    parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Log file to parse (or stdin)')
    parser.add_argument('-f', '--first', type=int, help='Print the first NUM lines')
    parser.add_argument('-l', '--last', type=int, help='Print the last NUM lines')
    parser.add_argument('-t', '--timestamps', action='store_true', help='Print lines containing a timestamp')
    parser.add_argument('-i', '--ipv4', action='store_true', help='Print lines containing an IPv4 address')
    parser.add_argument('-I', '--ipv6', action='store_true', help='Print lines containing an IPv6 address')
    
    try:
        args = parser.parse_args()
    except SystemExit:
        print("\nError: One or more arguments are invalid. Use `-h` for help.")
        sys.exit(1)


     # Check for conflicting options
    if args.first and args.last:
        print("Error: --first and --last options cannot be used together.")
        sys.exit(1)

    # Check if no valid options are provided
    if not any([args.first, args.last, args.ipv4, args.ipv6, args.timestamps]):
        print("Error: No valid options provided. Use -h for help.")
        sys.exit(1)

   

    # Read all lines from the file
    lines = args.file.readlines()

    if not lines:
        print("No input provided. Please provide a log file or use standard input.")
        sys.exit(1)

    # Apply filters sequentially
    if args.first:
        lines = get_first_n_lines(lines, args.first)
    if args.last:
        lines = get_last_n_lines(lines, args.last)
    if args.ipv4:
        lines = filter_ipv4_lines(lines)
    if args.ipv6:
        lines = filter_ipv6_lines(lines)
    if args.timestamps:
        lines = filter_timestamp_lines(lines)

    # Print the filtered lines
    if lines:
        for line in lines:
            print(line.strip())
    else:
        print("No matching results found.")

# Entry point of the script
if __name__ == "__main__":
    main()

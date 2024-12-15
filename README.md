# Log Parsing Utility - v1.01

## Description

This Python CLI application is designed to help you parse log files efficiently. 
The tool supports various filtering options, such as printing the first or last N lines, filtering lines containing IPv4 or IPv6 addresses, 
and extracting lines with timestamps. The application is easy to deploy and run, with a test suite included to ensure correctness.

This solution does not use the `head`, `tail`, or `grep` utilities and relies on custom Python functions to perform the required parsing. 
It supports multiple filtering options, allowing you to refine your log analysis.

## Features

- **Print the first N lines** of a log file
- **Print the last N lines** of a log file
- **Filter lines containing a timestamp** in HH:MM:SS format
- **Filter lines containing an IPv4 address**
- **Filter lines containing an IPv6 address**
- **Command-line interface** with user-friendly options
- **Supports multiple filters** at once, yielding the intersection of their results

## Usage

### Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/KalyaniGedela9/log-parsing-utility.git
   
   cd log-parsing-utility

2. **Create a virtual environment** (recommended to avoid conflicts with system packages)

        python3 -m venv venv

3.**Activate the virtual environment**

    	On Windows:
    		venv\Scripts\activate
    	
    	On macOS/Linux:
    		source venv/bin/activate
		
4. **Install dependencies**

	    pip install -r requirements.txt
	
##  Available Options

    -f, --first N       Print the first N lines from the log file.
    
    -l, --last N	    Print the last N lines from the log file.
   
    -t, --timestamps	Print lines containing timestamps in HH:MM:SS format.
    
    -i, --ipv4	        Print lines containing IPv4 addresses.
    
    -I, --ipv6	        Print lines containing IPv6 addresses.


### Example Usage
	
     Display help                                               ./util.py -h.
    
     Print the first 10 lines of log file**                     type <log file> | ./util.py --first 10 [type for command prompt]
     
     Print the last 5 lines of log file                         ./util.py --last 5 <log file>
     
     Print lines containing timestamps from log file            ./util.py --timestamps <log file>
     
     Print lines containing IPv4 addresses from log file        ./util.py --ipv4 <log file> /
     
     Print lines containing IPv6 addresses from log file        ./util.py -I/--ipv6 <log file>
		

     Multiple Options
	    Print the last 5 lines containing IPv4 addresses from log file        ./util.py -i/--ipv4 --last 50 <log file>

###    Code Structure
    log_parshing-utility/
		|-- log_parshing/
			  |-- util.py				     
			  |-- test_util.py		     
			  |-- Sample.log			    
	  |-- requirements.txt		   

### Testing
    **Run the test suite using `pytest`**
        pytest -s test_util.py
            
    **Expected output**
        All tests should pass with details of execution.
	
## Error Handling
1. **Invalid Arguments**: Displays an error message and exits.
2. **Conflicting Options**: Prompts the user to resolve conflicts, such as using both `--first` and `--last`.
3. **Empty Input**: Alerts the user if no log data is provided.


### Sample Log File
A sample log file is provided for testing purposes. You can find it in the repository under the filename **Sample.log.** 
Use this file to test and explore the functionality of the log parsing utility.

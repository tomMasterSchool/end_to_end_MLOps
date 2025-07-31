'''
This script sets up a logging system for a Python application. It performs the following:

1. Imports necessary modules: 
   - `os` for file/directory operations,
   - `sys` for system I/O (like printing to the console),
   - `logging` for generating log messages.

2. Defines a custom log format `logging_str` that includes the timestamp, log level, module name, and the actual message.

3. Sets up a directory named 'logs' and a log file path inside it ('running_logs.log').

4. Creates the 'logs' directory if it doesn't exist using `os.makedirs()`.

5. Configures the logging system using `logging.basicConfig()` to:
   - Set the logging level to INFO,
   - Use the custom format,
   - Log messages both to a file (for persistent storage) and to the console (for real-time feedback).

This setup allows developers to track what happens during the execution of their program, making it easier to debug and monitor behavior.
'''

# Importing the os module to work with file and directory paths
import os

# Importing the sys module to access system-specific parameters and functions (like stdout)
import sys

# Importing the logging module to set up logging for the application
import logging

# Defining the format of log messages, including time, log level, module name, and the actual message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Setting the directory where log files will be stored
log_dir = "logs"

# Defining the full path to the log file
log_filepath = os.path.join(log_dir, "running_logs.log")

# Creating the log directory if it doesn't already exist
os.makedirs(log_dir, exist_ok=True)

# Configuring the logging module with level, format, and handlers
logging.basicConfig(
    level=logging.INFO,           # Sets the logging level to INFO
    format=logging_str,           # Uses the custom format defined earlier
    handlers=[
        logging.FileHandler(log_filepath),  # Logs messages to a file
        logging.StreamHandler(sys.stdout)   # Also prints log messages to the console
    ]
)

# How to write Python program exceptions to the log file:

# By using the following function, we can write exception information to the log file:
# logging.exception(msg)

# Python Program to write exception information to the log file:

import logging

# Configure logging to write log messages to 'mylog.txt' file with specified settings
logging.basicConfig(
    filename='mylog.txt',               # Log file name
    level=logging.INFO,                # Logging level set to INFO
    format='%(asctime)s:%(levelname)s:%(message)s',  # Log message format
    datefmt='%d/%m/%Y %I:%M:%S %p'     # Date and time format
)

# Log a message to indicate a new request
logging.info('A new Request Came')

try:
    # Attempt to perform some operations that might raise exceptions
    x = int(input('Enter First Number:'))
    y = int(input('Enter Second Number:'))
    result = x / y
    print('The Result:', result)

except ZeroDivisionError as msg:
    # Handle the ZeroDivisionError exception and log the exception message
    print('Cannot divide with zero')
    logging.exception(msg)

except ValueError as msg:
    # Handle the ValueError exception and log the exception message
    print('Please provide int values only')
    logging.exception(msg)

# Log a message to indicate that request processing is completed
logging.info('Request Processing Completed')

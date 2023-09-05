# Python Logging

# It is highly recommended to store complete application flow and exceptions information to a file.
# This process is called logging.
# The main advantages of logging are:
# 1. We can use log files while performing debugging.
# 2. We can provide statistics like the number of requests per day, etc.
# To implement logging, Python provides an inbuilt module, logging.

# Logging Levels:
# Depending on the type of information, logging data is divided into the following 6 levels in Python:
# 1. CRITICAL ===> 50
#    Represents a very serious problem that needs high attention.
# 2. ERROR ===> 40
#    Represents a serious error.
# 3. WARNING ==> 30
#    Represents a warning message; some caution is needed. It is an alert to the programmer.
# 4. INFO ==> 20
#    Represents a message with some important information.
# 5. DEBUG ===> 10
#    Represents a message with debugging information.
# 6. NOTSET ==> 0
#    Represents that the level is not set.
# By default, while executing a Python program, only WARNING and higher-level messages will be displayed.

# How to implement Logging:
# To perform logging, we first need to create a file to store messages and specify which level messages need to be stored.
# We can do this by using the basicConfig() function of the logging module.
# Example:
# logging.basicConfig(filename='log.txt', level=logging.WARNING)
# The above line will create a file 'log.txt' and store either WARNING level or higher-level messages in that file.

# After creating the log file, we can write messages to it using the following methods:
# - logging.debug(message)
# - logging.info(message)
# - logging.warning(message)
# - logging.error(message)
# - logging.critical(message)

# Example: Write a Python Program to create a log file and write WARNING and higher-level messages.
import logging

# Create a log file named 'log.txt' and store WARNING and higher-level messages
logging.basicConfig(filename='log.txt', level=logging.WARNING)

# Print a message to the console
print('Logging Demo')

# Log messages of different levels
logging.debug('Debug Information')  # This will not be written to the log file
logging.info('Info Information')    # This will not be written to the log file
logging.warning('Warning Information')  # This will be written to the log file
logging.error('Error Information')      # This will be written to the log file
logging.critical('Critical Information')  # This will be written to the log file

# How to Format log messages:

# By using the 'format' keyword argument, we can format log messages in different ways.

# Example 1: To display only the level name
# logging.basicConfig(format='%(levelname)s')
# Output:
# WARNING
# ERROR
# CRITICAL

# Example 2: To display the level name and message
# logging.basicConfig(format='%(levelname)s:%(message)s')
# Output:
# WARNING:warning Information
# ERROR:error Information
# CRITICAL:critical Information

# How to add a timestamp in the log messages:
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
# Output:
# 2018-06-15 11:50:08,325:WARNING:warning Information
# 2018-06-15 11:50:08,372:ERROR:error Information
# 2018-06-15 11:50:08,372:CRITICAL:critical Information

# How to change the date and time format:
# We can use the special keyword argument 'datefmt'.
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
# datefmt='%d/%m/%Y %I:%M:%S %p' ===> Case is important
# Output:
# 15/06/2018 12:04:31 PM:WARNING:warning Information
# 15/06/2018 12:04:31 PM:ERROR:error Information
# 15/06/2018 12:04:31 PM:CRITICAL:critical Information

# Note:
# - %I ---> means 12 Hours time scale
# - %H ---> means 24 Hours time scale

# Example:
# logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# Output:
# 15/06/2018 12:06:28:WARNING:warning Information
# 15/06/2018 12:06:28:ERROR:error Information
# 15/06/2018 12:06:28:CRITICAL:critical Information

import logging

# Configure logging with a specific log message format and date format
logging.basicConfig(
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%d/%m/%Y %I:%M:%S %p'  # Change the date and time format
)

# Print log messages with different levels
print('Logging Demo')
logging.debug('Debug Information')       # Debug level message
logging.info('Info Information')         # Info level message
logging.warning('Warning Information')   # Warning level message
logging.error('Error Information')       # Error level message
logging.critical('Critical Information') # Critical level message

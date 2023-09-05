# How to configure log file in overwriting mode:

# By default, data will be appended to the log file, i.e., 'append' is the default mode.
# Instead of appending, if we want to overwrite data, we have to use the 'filemode' property.

# Example:
# logging.basicConfig(filename='newlog.txt', level=logging.WARNING)
#   - This is meant for appending (default behavior).

# logging.basicConfig(filename='newlog.txt', level=logging.WARNING, filemode='a')
#   - Here, we are explicitly specifying appending.

# logging.basicConfig(filename='newlog.txt', level=logging.WARNING, filemode='w')
#   - This is meant for overwriting the previous data.

# Note:
# - If we are not specifying the level, then the default level is WARNING (level 30).
# - If we are not specifying the file name, then the messages will be printed to the console.

import logging

# Configure logging to overwrite data in 'newlog.txt'
logging.basicConfig(filename='newlog.txt', level=logging.WARNING, filemode='w')

# Print a message to the console
print('Logging Demo')

# Log messages of different levels
logging.debug('Debug Information')       # This will not be written to the log file
logging.info('Info Information')         # This will not be written to the log file
logging.warning('Warning Information')   # This will be written to the log file
logging.error('Error Information')       # This will be written to the log file
logging.critical('Critical Information') # This will be written to the log file

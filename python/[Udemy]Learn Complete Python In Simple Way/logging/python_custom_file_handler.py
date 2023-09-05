import logging  # Import the logging module

# Create a customized logger named 'demologger'.
logger = logging.getLogger('demologger')

# Set the log level for our customized logger to DEBUG.
logger.setLevel(logging.DEBUG)

# Create a file handler for our logger. This handler will write log messages to a file named 'custtest.log'.
# The 'mode' parameter is set to 'w', which means the file will be opened in write mode (overwriting existing content).
fileHandler = logging.FileHandler('custtest.log', mode='w')

# Create a log message formatter with a specific format, including timestamp, logger name, and log level.
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

# Set the formatter for the file handler.
fileHandler.setFormatter(formatter)

# Add the file handler to our customized logger.
logger.addHandler(fileHandler)

# Now we can write log messages at different levels using our customized logger.
logger.critical('It is a critical message')
logger.error('It is an error message')
logger.warning('It is a warning message')
logger.info('It is an info message')
logger.debug('It is a debug message')

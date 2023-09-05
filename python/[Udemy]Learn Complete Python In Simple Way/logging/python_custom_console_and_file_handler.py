import logging  # Import the logging module

# Create a customized logger named 'demo logger'.
logger = logging.getLogger('demo logger')

# Set the log level for our customized logger to INFO.
logger.setLevel(logging.INFO)

# Create a console handler for our logger. This handler will write log messages to the console.
consoleHandler = logging.StreamHandler()

# Create a file handler for our logger. This handler will write log messages to a file named 'abc.log'.
# The 'mode' parameter is set to 'w', which means the file will be opened in write mode (overwriting existing content).
fileHandler = logging.FileHandler('abc.log', mode='w')

# Create a log message formatter with a specific format, including timestamp, logger name, and log level.
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

# Set the formatter for the console handler.
consoleHandler.setFormatter(formatter)

# Set the formatter for the file handler.
fileHandler.setFormatter(formatter)

# Add both the console handler and file handler to our customized logger.
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

# Now we can write log messages at different levels using our customized logger.
logger.critical('It is a critical message')
logger.error('It is an error message')
logger.warning('It is a warning message')
logger.info('It is an info message')
logger.debug('It is a debug message')

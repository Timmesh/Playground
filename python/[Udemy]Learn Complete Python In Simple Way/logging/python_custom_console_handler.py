import logging  # Import the logging module

# The root logger has some limitations, so we create our own customized logger named 'demologger'.
logger = logging.getLogger('demologger')

# We set the log level for our customized logger to INFO.
logger.setLevel(logging.INFO)

# Create a console handler for our logger. This handler will output log messages to the console.
consoleHandler = logging.StreamHandler()

# Create a log message formatter with a specific format, including timestamp, logger name, and log level.
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

# Set the formatter for the console handler.
consoleHandler.setFormatter(formatter)

# Add the console handler to our customized logger.
logger.addHandler(consoleHandler)

# Now we can write log messages at different levels using our customized logger.
logger.critical('It is a critical message')
logger.error('It is an error message')
logger.warning('It is a warning message')
logger.info('It is an info message')
logger.debug('It is a debug message')

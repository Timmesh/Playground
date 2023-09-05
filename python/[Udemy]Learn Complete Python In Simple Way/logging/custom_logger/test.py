from custlogger import get_custom_logger
import logging

# Define a function for testing the custom logger.
def logtest():
    # Create a custom logger with DEBUG log level.
    logger = get_custom_logger(logging.DEBUG)

    # Log messages at different levels using the custom logger.
    logger.critical('critical message from test module')
    logger.error('error message from test module')
    logger.warning('warning message from test module')
    logger.info('info message from test module')
    logger.debug('debug message from test module')

# Call the logtest function to test the custom logger.
logtest()

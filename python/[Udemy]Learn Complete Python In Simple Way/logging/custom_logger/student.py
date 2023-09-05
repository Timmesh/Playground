from custlogger import get_custom_logger
import logging

# Define a function for testing the custom logger in a different module.
def logstudent():
    # Create a custom logger with ERROR log level.
    logger = get_custom_logger(logging.ERROR)

    # Log messages at different levels using the custom logger.
    logger.critical('critical message from student module')
    logger.error('error message from student module')
    logger.warning('warning message from student module')
    logger.info('info message from student module')
    logger.debug('debug message from student module')

# Call the logstudent function to test the custom logger in a different module.
logstudent()

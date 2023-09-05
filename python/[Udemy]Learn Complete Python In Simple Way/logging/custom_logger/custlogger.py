import logging
import inspect

# Define a function to create a custom logger based on the calling function's name and a specified logging level.
def get_custom_logger(level):
    # Get the name of the calling function using the inspect module.
    function_name = inspect.stack()[1][3]
    # Create a logger name by appending " logger" to the function name.
    logger_name = function_name + " logger"

    # Create a logger instance with the generated logger name.
    logger = logging.getLogger(logger_name)
    # Set the log level for this logger.
    logger.setLevel(level)

    # Create a file handler for logging to a file named 'abc.log'.
    fileHandler = logging.FileHandler('../abc.log', mode='a')
    fileHandler.setLevel(level)

    # Define the log message format, including timestamp, log level, logger name, and message.
    formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)

    # Add the file handler to the logger.
    logger.addHandler(fileHandler)

    # Return the customized logger.
    return logger

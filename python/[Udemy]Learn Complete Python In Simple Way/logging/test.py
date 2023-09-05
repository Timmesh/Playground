# test.py

import student  # Importing the student module
import logging

# In student.py, we configure logging using basicConfig to write log messages to student.log with a logging level of INFO.
# In test.py, we configure logging again using basicConfig to write log messages to test.log with a logging level of DEBUG.
# When we import the student module in test.py, it inherits the logging configuration from the root logger.
# As a result, the logging configuration performed in test.py doesn't affect the student module's logging configuration.

# Configuring logging in the test module
logging.basicConfig(filename='test.log', level=logging.DEBUG)
logging.debug('debug message from test module')

# The problem here is that once we perform basic configuration to the root logger in student.py,
# the configurations are fixed and cannot be changed, which may not be suitable for more complex
# applications where different parts of the code require different logging configurations.


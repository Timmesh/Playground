from custlogger import get_custom_logger
import logging

def f1():
    logger = get_custom_logger(logging.DEBUG)
    logger.critical('critical message from f1')
    logger.error('error message from f1')
    logger.warning('warning message from f1')
    logger.info('info message from f1')
    logger.debug('debug message from f1')

def f2():
    logger = get_custom_logger(logging.WARNING)
    logger.critical('critical message from f2')
    logger.error('error message from f2')
    logger.warning('warning message from f2')
    logger.info('info message from f2')
    logger.debug('debug message from f2')

def f3():
    logger = get_custom_logger(logging.ERROR)
    logger.critical('critical message from f3')
    logger.error('error message from f3')
    logger.warning('warning message from f3')
    logger.info('info message from f3')
    logger.debug('debug message from f3')

f1()
f2()
f3()

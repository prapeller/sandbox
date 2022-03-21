import logging
import sys
from logging.handlers import TimedRotatingFileHandler

from settings import SERVER_LOG_FORMAT, SERVER_LOG_FILE_PATH, GLOBAL_LOG_LEVEL

CONSOLE_HANDLER = logging.StreamHandler(sys.stderr)
CONSOLE_HANDLER.setFormatter(SERVER_LOG_FORMAT)
CONSOLE_HANDLER.setLevel(logging.ERROR)

FILE_HANDLER = TimedRotatingFileHandler(SERVER_LOG_FILE_PATH, encoding='utf8', interval=1, when='MIDNIGHT')
FILE_HANDLER.setFormatter(SERVER_LOG_FORMAT)

LOGGER = logging.getLogger('Server')
LOGGER.addHandler(CONSOLE_HANDLER)
LOGGER.addHandler(FILE_HANDLER)
LOGGER.setLevel(GLOBAL_LOG_LEVEL)

if __name__ == '__main__':
    LOGGER.debug('Debug message')
    LOGGER.info('Info message')
    LOGGER.warning('Warning message')
    LOGGER.error('Error message')
    LOGGER.critical('Critical message')
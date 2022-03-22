import logging
import sys

from settings import CLIENT_LOG_FORMAT, CLIENT_LOG_FILE_PATH, GLOBAL_LOG_LEVEL

CONSOLE_HANDLER = logging.StreamHandler(sys.stderr)
CONSOLE_HANDLER.setFormatter(CLIENT_LOG_FORMAT)
CONSOLE_HANDLER.setLevel(logging.INFO)

FILE_HANDLER = logging.FileHandler(CLIENT_LOG_FILE_PATH, encoding="utf8")
FILE_HANDLER.setFormatter(CLIENT_LOG_FORMAT)

LOGGER = logging.getLogger("Client")
LOGGER.addHandler(CONSOLE_HANDLER)
LOGGER.addHandler(FILE_HANDLER)
LOGGER.setLevel(GLOBAL_LOG_LEVEL)

if __name__ == "__main__":
    LOGGER.debug("Debug message")
    LOGGER.info("Info message")
    LOGGER.warning("Warning message")
    LOGGER.error("Error message")
    LOGGER.critical("Critical message")

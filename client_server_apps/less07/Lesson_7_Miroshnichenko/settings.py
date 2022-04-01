import logging
from pathlib import Path

BASEDIR = Path(__file__).resolve().parent

SERVER_ADDRESS = "localhost"
SERVER_PORT = 8888
CONNECTIONS_NUMBER_MAX = 5
BUFFER_SIZE = 1024
ENCODING = "utf-8"

CLIENT_LOG_FORMAT = logging.Formatter("%(asctime)s | %(levelname)-8s | %(filename)-15s | %(message)s")
CLIENT_LOG_FILE_PATH = BASEDIR / "project_logs/logs/client.log"

SERVER_LOG_FORMAT = logging.Formatter("%(asctime)s | %(levelname)-8s | %(filename)-15s | %(message)s")
SERVER_LOG_FILE_PATH = BASEDIR / "project_logs/logs/server.log"

GLOBAL_LOG_LEVEL = logging.DEBUG

# ===============================
#           JIM Protocol keys:
# ===============================

ACTION = "action"
TIME = "time"
USER = "user"
ACCOUNT_NAME = "account_name"

PRESENCE = "presence"
RESPONSE = "response"
ERROR = "error"

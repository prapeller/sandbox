import json
import logging
import socket
import time
import inspect

from settings import BUFFER_SIZE, ENCODING, ACTION, ACCOUNT_NAME, TIME, PRESENCE, USER, RESPONSE, ERROR
from project_logs.config import config_log_client, config_log_server


def log_method(method):
    """Decorator for logging methods of the "Server" and "Client" classes:
    """

    def wrapper(*args, **kwargs):
        instance = args[0]
        class_name = instance.__class__.__name__

        if class_name == "Server":
            logger = logging.getLogger("Server")
        elif class_name == "Client":
            logger = logging.getLogger("Client")
        else:
            raise ValueError(f"{instance} should be inherited from classes with classname \"Server\" or \"Client\"")
        # logger.debug(f'from module: {method.__module__}, from function: {inspect.stack()[1][3]}, called method: {method} with params: {args}, {kwargs}', stacklevel=2)
        logger.debug(f'"{class_name}" called "{method.__name__}" with params: {args}, {kwargs}', stacklevel=2)
        return method(*args, **kwargs)

    return wrapper


def bind_logger_to_class(cls):
    """Decorator for binding server/client logger to mixin
    in accordance with name of class that using mixin"""

    def decorate(__init__):
        def new_init(self, *args, **kwargs):
            if self.__class__.__name__ == "Server":
                self.logger = logging.getLogger("Server")
            elif self.__class__.__name__ == "Client":
                self.logger = logging.getLogger("Client")
            else:
                raise ValueError(f"{cls.__name__} should be inherited from classes with classname \"Server\" or \"Client\"")
            super(cls, self).__init__(*args, **kwargs)

        return new_init

    cls.__init__ = decorate(cls.__init__)

    return cls


@bind_logger_to_class
class ValidatorMixin:
    """Mixin for using in __init__ methods of child classes
    validating used ports, must be within [1024:65535]"""

    @log_method
    def validate_port(self, port: int):
        if port < 1024 or port > 65535:
            self.logger.critical(f"{self} cant validate port {port}, it must be within [1024:65535]")
            raise ValueError()


@bind_logger_to_class
class MessengerMixin:
    """Mixin for using in Server and Client classes
    implementing send_message/receive_message methods
    and helping methods for messaging"""

    @log_method
    def create_presence_message(self, account_name="Guest") -> dict:
        """
        Returns dict with presence_message for current client, for not registered account "account_name" is "Guest":
        {"action": "presence", "time": 1573760672.167031, "user": {"account_name": "Guest"}}
        """
        message = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: account_name
            }
        }

        self.logger.debug(f"{self} creating presence message {message}")
        return message

    @log_method
    def receive_message(self, transport: socket.socket) -> dict:
        try:
            message_bytes = transport.recv(BUFFER_SIZE)
            message_json = message_bytes.decode(ENCODING)
            message = json.loads(message_json)
            self.logger.debug(f"{transport} receiving message: {message}")

            return message
        except Exception as e:
            self.logger.debug(f"critical in {self}: {e}")
            transport.close()

    @log_method
    def send_message(self, transport: socket.socket, message: dict) -> None:
        try:
            message_json = json.dumps(message)
            message_bytes = message_json.encode(ENCODING)
            transport.send(message_bytes)
            self.logger.debug(f"{transport} sending as encoded message: {message}")
        except Exception as e:
            self.logger.debug(f"{self} can't send message: {e}")
            transport.close()

    @log_method
    def get_response(self, message: dict) -> dict:
        """parsing and returning response from message"""
        if all((
                (ACTION in message),
                (message.get(ACTION) == PRESENCE),
                (USER in message and message.get(USER).get(ACCOUNT_NAME) == "Guest"),
                (TIME in message),
        )):
            response = {RESPONSE: 200}
        else:
            response = {
                RESPONSE: 400,
                ERROR: "Bad Request"
            }
        self.logger.debug(f"{self} got response: {response} from message:{message}")
        return response

    @log_method
    def get_response_code(self, message: dict) -> str:
        response_code = None
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                response_code = "200 : OK"
            elif message[RESPONSE] == 400:
                response_code = f"400 : {message[ERROR]}"

            self.logger.info(f"{self} got response_code: \"{response_code}\" from message: {message}")
            return response_code
        else:
            self.logger.critical(f"{self}, can't get response_code from message: {message}")
            raise ValueError

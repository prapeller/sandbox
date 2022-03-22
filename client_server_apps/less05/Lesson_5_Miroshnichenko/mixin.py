import json
import logging
import socket
import time

from settings import BUFFER_SIZE, ENCODING, ACTION, ACCOUNT_NAME, TIME, PRESENCE, USER, RESPONSE, ERROR
from project_logs.config import config_log_client, config_log_server


def bind_logger(cls, instance):
    """Binding server/client logger to mixin in accordance with child class name"""
    if instance.__class__.__name__ == "Server":
        instance.logger = logging.getLogger("Server")
    elif instance.__class__.__name__ == "Client":
        instance.logger = logging.getLogger("Client")
    else:
        raise Exception(f"{cls.__name__} should be inherited from classes with classname \"Server\" or \"Client\"")


class ValidatorMixin:
    """Mixin for using in __init__ methods of child classes
    validating used ports, must be within [1024:65535]"""

    def __init__(self, *args, **kwargs):
        self.logger = None
        bind_logger(cls=self.__class__, instance=self)
        super().__init__(*args, **kwargs)

    def validate_port(self, port: int):
        if port < 1024 or port > 65535:
            self.logger.critical(f"{self} cant validate port {port}, it must be within [1024:65535]")
            raise ValueError()


class MessengerMixin:
    """Mixin for using in Server and Client classes
    implementing send_message/receive_message methods
    and helping methods for messaging"""

    def __init__(self, *args, **kwargs):
        self.logger = None
        bind_logger(cls=self.__class__, instance=self)
        super().__init__(*args, **kwargs)

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

    def send_message(self, transport: socket.socket, message: dict) -> None:
        try:
            message_json = json.dumps(message)
            message_bytes = message_json.encode(ENCODING)
            transport.send(message_bytes)
            self.logger.debug(f"{transport} sending as encoded message: {message}")
        except Exception as e:
            self.logger.debug(f"{self} can't send message: {e}")
            transport.close()

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

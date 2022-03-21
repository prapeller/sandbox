import json
import logging
import socket
import time

from settings import BUFFER_SIZE, ENCODING, ACTION, ACCOUNT_NAME, TIME, PRESENCE, USER, RESPONSE, ERROR
from project_logs.config import config_log_client, config_log_server


class ValidatorMixin:

    def validate_port(self, port: int):
        if port < 1024 or port > 65535:
            log_info = f'{self} cant validate port {port}, it must be within [1024:65535]'
            logging.getLogger(self.__class__.__name__).critical(log_info)
            raise ValueError()


class MessengerMixin:
    def create_presence_message(self, account_name='Guest') -> dict:
        """
        Returns dict with presence_message for current client, for not registered account 'account_name' is 'Guest':
        {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
        """
        message = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: account_name
            }
        }

        logging.getLogger(self.__class__.__name__).debug(f'{self} creating presence message {message}')
        return message

    def receive_message(self, transport: socket.socket) -> dict:
        try:
            message_bytes = transport.recv(BUFFER_SIZE)
            message_json = message_bytes.decode(ENCODING)
            message = json.loads(message_json)
            logging.getLogger(self.__class__.__name__).debug(f'{transport} receiving message: {message}')

            return message
        except Exception as e:
            logging.getLogger(self.__class__.__name__).debug(f'critical in {self}: {e}')
            transport.close()

    def send_message(self, transport: socket.socket, message: dict) -> None:
        try:
            message_json = json.dumps(message)
            message_bytes = message_json.encode(ENCODING)
            transport.send(message_bytes)
            logging.getLogger(self.__class__.__name__).debug(f'{transport} sending as encoded message: {message}')
        except Exception as e:
            logging.getLogger(self.__class__.__name__).debug(f'critical in {self}: {e}')
            transport.close()

    def get_response(self, message: dict) -> dict:
        if all((
                (ACTION in message),
                (message.get(ACTION) == PRESENCE),
                (USER in message and message.get(USER).get(ACCOUNT_NAME) == 'Guest'),
                (TIME in message),
        )):
            response = {RESPONSE: 200}
        else:
            response = {
                RESPONSE: 400,
                ERROR: 'Bad Request'
            }
        logging.getLogger(self.__class__.__name__).debug(f'{self} got response: {response} from {message}')
        return response

    def get_response_code(self, message: dict) -> str:
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                response_code = '200 : OK'
            elif message[RESPONSE] == 400:
                response_code = f'400 : {message[ERROR]}'

            logging.getLogger(self.__class__.__name__).info(f'{self} got response_code: "{response_code}" from {message}')
            return response_code
        else:
            logging.getLogger(self.__class__.__name__).critical(f'critical with {self}, cant get response_code from {message}')
            raise ValueError

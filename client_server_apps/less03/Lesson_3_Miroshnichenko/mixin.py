import json
import time

from settings import BUFFER_SIZE, ENCODING, ACTION, ACCOUNT_NAME, TIME, PRESENCE, USER, RESPONSE, ERROR


class ValidatorMixin:
    @staticmethod
    def validate_port(port):
        if port < 1024 or port > 65535:
            raise ValueError('port must be within [1024:65535]')


class MessengerMixin:
    @staticmethod
    def create_presence_message(account_name='Guest') -> dict:
        """
        Returns dict with presence_message for current client, for not registered account 'account_name' is 'Guest':
        {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
        """
        return {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: account_name
            }
        }

    @staticmethod
    def receive_message(transport) -> dict:
        try:
            message_bytes = transport.recv(BUFFER_SIZE)
            message_json = message_bytes.decode(ENCODING)
            message = json.loads(message_json)
            print(f'{transport} receiving message: {message}')
            return message
        except Exception as e:
            print(e)
            transport.close()

    @staticmethod
    def send_message(transport, message):
        try:
            message_json = json.dumps(message)
            message_bytes = message_json.encode(ENCODING)
            transport.send(message_bytes)
        except Exception as e:
            print(e)
            transport.close()

    @staticmethod
    def get_response(message: dict) -> dict:
        if all((
                (ACTION in message),
                (message[ACTION] == PRESENCE),
                (USER in message),
                (message[USER][ACCOUNT_NAME] == 'Guest'),
                (TIME in message),
        )):
            return {RESPONSE: 200}
        return {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }

    @staticmethod
    def get_response_code(message: dict) -> str:
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return '200 : OK'
            return f'400 : {message[ERROR]}'
        raise ValueError

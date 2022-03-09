import json

from settings import BUFFER_SIZE, ENCODING, ACTION, ACCOUNT_NAME, TIME, PRESENCE, USER, RESPONSE, ERROR

class ValidatorMixin:
    @staticmethod
    def validate_port(port):
        if port < 1024 or port > 65535:
            raise ValueError('port must be within [1024:65535]')



class MessengerMixin:
    @staticmethod
    def receive_message_from(sender) -> dict:
        data_bytes = sender.recv(BUFFER_SIZE)
        response_json = data_bytes.decode(ENCODING)
        response_dict = json.loads(response_json)
        return response_dict

    @staticmethod
    def send_message_to(recipient, message):
        message_json = json.dumps(message)
        message_bytes = message_json.encode(ENCODING)
        recipient.send(message_bytes)

    @staticmethod
    def get_response_code(message: dict) -> dict:
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

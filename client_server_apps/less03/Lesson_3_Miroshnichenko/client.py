from socket import socket, AF_INET, SOCK_STREAM
import json
import time
from base import MessengerMixin, ValidatorMixin
from settings import (ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, SERVER_ADDRESS, SERVER_PORT)


class Client(MessengerMixin, ValidatorMixin, socket):

    def create_presence_message(account_name='Guest') -> dict:
        # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
        return {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: account_name
            }
        }

    def get_response_code(message: dict):
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return '200 : OK'
            return f'400 : {message[ERROR]}'
        raise ValueError


    def run(self):
        server_sock = socket(AF_INET, SOCK_STREAM)
        server_sock.connect(SERVER_ADDRESS)
        message = self.create_presence_message()
        self.send_message_to(server_sock, message)
        try:
            message_received = self.receive_message_from(server_sock)
            response_code = self.get_response_code(message_received)
            print(response_code)
        except (ValueError, json.JSONDecodeError):
            print('Cant decode server message')

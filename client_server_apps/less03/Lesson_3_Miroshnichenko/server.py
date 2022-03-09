import socket
from socket import AF_INET, SOCK_STREAM
import json

from base import MessengerMixin, ValidatorMixin
from settings import SERVER_ADDRESS, SERVER_PORT, CONNECTIONS_NUMBER_MAX


class Server(MessengerMixin, ValidatorMixin, socket.socket):
    def __init__(self, addr=SERVER_ADDRESS, port=SERVER_PORT):
        self.validate_port(port)
        super().__init__(family=AF_INET, type=SOCK_STREAM)
        self.bind((addr, port))
        self.listen(CONNECTIONS_NUMBER_MAX)

    def run(self):
        while True:
            client, client_address = self.accept()
            try:
                message = self.receive_message_from(client)
                print(f'{self} received message from {client}:\n{message}')
                # {'action': 'presence', 'time': 1573760672.167031, 'user': {'account_name': 'Guest'}}
                response = self.get_response_code(message)
                self.send_message_to(client, response)
                client.close()
            except (ValueError, json.JSONDecodeError):
                print('It was received invalid message from client.')
                client.close()

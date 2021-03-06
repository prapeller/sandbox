import logging
from socket import socket, AF_INET, SOCK_STREAM
from mixin import MessengerMixin, ValidatorMixin
from settings import SERVER_ADDRESS, SERVER_PORT
from project_logs.config import config_log_client


class Client(MessengerMixin, ValidatorMixin, socket):
    def __init__(self, port=SERVER_PORT):
        self.logger = logging.getLogger("Client")
        self.validate_port(port)
        super().__init__(family=AF_INET, type=SOCK_STREAM)
        self.logger.debug(f"{self} was initialized")

    def run(self):
        self.connect((SERVER_ADDRESS, SERVER_PORT))
        presence_message = self.create_presence_message()
        self.send_message(self, presence_message)
        response = self.receive_message(self)
        response_code = self.get_response_code(response)
        print(response_code)


if __name__ == "__main__":
    client = Client()
    client.run()

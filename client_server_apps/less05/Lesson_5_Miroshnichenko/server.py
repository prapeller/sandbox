import socket
from socket import AF_INET, SOCK_STREAM

from mixin import MessengerMixin, ValidatorMixin
from settings import SERVER_ADDRESS, SERVER_PORT, CONNECTIONS_NUMBER_MAX


class Server(MessengerMixin, ValidatorMixin, socket.socket):
    def __init__(self, addr=SERVER_ADDRESS, port=SERVER_PORT):
        self.validate_port(port)
        super().__init__(family=AF_INET, type=SOCK_STREAM)
        self.bind((addr, port))
        self.listen(CONNECTIONS_NUMBER_MAX)

    def run(self):
        while True:
            client_sock, client_address = self.accept()
            message = self.receive_message(client_sock)
            response = self.get_response(message)
            self.send_message(client_sock, response)
            client_sock.close()


if __name__ == '__main__':
    server = Server()
    server.run()

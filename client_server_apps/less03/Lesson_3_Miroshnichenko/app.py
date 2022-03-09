from server import Server
from client import Client

if __name__ == '__main__':
    server = Server()
    server.run()

    client = Client()
    client.run()

from subprocess import Popen, PIPE
from unittest import TestCase

from server import Server
from ..client import Client
from settings import TIME, ACTION, PRESENCE, USER, ACCOUNT_NAME, RESPONSE, ERROR


class TestClient(TestCase):
    def setUp(self) -> None:
        self.server = Server()
        self.client = Client()

    def tearDown(self) -> None:
        self.server.close()
        self.client.close()

    def test_validate_port(self):
        """Test Client with wrong port doesn't pass validation while __init__ ('port must be within [1024:65535]')"""
        with self.assertRaises(ValueError):
            Client(port=1023)
        with self.assertRaises(ValueError):
            Client(port=65536)

    def test_create_presence_message(self):
        """Test client creating correct presence message"""
        message = self.client.create_presence_message()
        message[TIME] = None
        self.assertEqual(message, {ACTION: PRESENCE, TIME: None, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_get_response_code_200(self):
        """Test client getting response code "200 : OK" from message"""
        message = {RESPONSE: 200}
        response_code = self.client.get_response_code(message)
        self.assertEqual(response_code, '200 : OK')

    def test_get_response_code_400(self):
        """Test client getting response code "400 : Bad Request" from message"""
        message = {RESPONSE: 400, ERROR: 'Bad Request'}
        response_code = self.client.get_response_code(message)
        self.assertEqual(response_code, '400 : Bad Request')

    def test_raises_error_without_response(self):
        """Test client raises ValueError if not RESPONSE in message"""
        message = {ERROR: 'Bad Request'}
        self.assertRaises(ValueError, self.client.get_response_code, message)

    # def test_client_send_message(self):
        # server_p = Popen(["python3.10", "server.py"], stdout=PIPE)
        # client_p = Popen(["python3.10", "client.py"], stdin=server_p.stdout, stdout=PIPE)
        # server_p.stdout.close()
        # client_p.communicate()
        # server_p.kill()
        # client_p.kill()

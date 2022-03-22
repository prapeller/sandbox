from unittest import TestCase

from ..server import Server
from ..settings import TIME, ACTION, PRESENCE, USER, ACCOUNT_NAME, RESPONSE, ERROR


# @staticmethod
# def get_response(message: dict) -> dict:
#     if all((
#             (ACTION in message),
#             (message[ACTION] == PRESENCE),
#             (USER in message),
#             (message[USER][ACCOUNT_NAME] == "Guest"),
#             (TIME in message),
#     )):
#         return {RESPONSE: 200}
#     return {RESPONSE: 400, ERROR: "Bad Request"}

class TestServer(TestCase):
    def setUp(self) -> None:
        self.server = Server()

        self.message_error = {
            RESPONSE: 400,
            ERROR: "Bad Request"
        }
        self.message_ok = {RESPONSE: 200}

    def tearDown(self) -> None:
        self.server.close()

    def test_get_response_to_message_ok(self):
        """Test Server getting response "message_ok" if all of the following conditions:
        (ACTION in message),
        (message[ACTION] == PRESENCE),
        (USER in message and message[USER][ACCOUNT_NAME] == "Guest"),
        (TIME in message)"""
        message = {ACTION: PRESENCE, TIME: None, USER: {ACCOUNT_NAME: "Guest"}}
        self.assertEqual(self.server.get_response(message), self.message_ok)
        self.server.close()

    def test_get_response_to_message_error_no_action(self):
        """Test Server getting response "message_error" if:
        (ACTION not in message)"""
        message = {TIME: None, USER: {ACCOUNT_NAME: "Guest"}}
        self.assertEqual(self.server.get_response(message), self.message_error)

    def test_get_response_to_message_error_action_no_presense(self):
        """Test Server getting response "message_error" if:
        (message[ACTION] != PRESENCE)"""
        message = {ACTION: None, TIME: None, USER: {ACCOUNT_NAME: "Guest"}}
        self.assertEqual(self.server.get_response(message), self.message_error)

    def test_get_response_to_message_error_no_user(self):
        """Test Server getting response "message_error" if:
        (USER not in message)"""
        message = {ACTION: PRESENCE, TIME: None}
        self.assertEqual(self.server.get_response(message), self.message_error)

    def test_get_response_to_message_error_no_guest(self):
        """Test Server getting response "message_error" if:
        (message[USER][ACCOUNT_NAME] != "Guest")"""
        message = {ACTION: PRESENCE, TIME: None, USER: {ACCOUNT_NAME: "Guests"}}
        self.assertEqual(self.server.get_response(message), self.message_error)

    def test_get_response_to_message_error_no_time(self):
        """Test Server getting response "message_error" if:
        (TIME not in message)"""
        message = {ACTION: PRESENCE, USER: {ACCOUNT_NAME: "Guest"}}
        self.assertEqual(self.server.get_response(message), self.message_error)

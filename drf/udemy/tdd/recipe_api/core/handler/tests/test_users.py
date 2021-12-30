from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

LIST_CREATE_USER_URL = reverse('users:list-create')


def create_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


class AnonymousUserApiTests(TestCase):
    """Test the anonymous users API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user(self):
        """Test creating user with valid payload at admin site is successful"""
        payload = {
            'email': 'test@email.com',
            'password': '123Testpassword',
        }
        resp = self.client.post(LIST_CREATE_USER_URL, payload)
        user = get_user_model().objects.get(**resp.data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', resp.data)

    def test_create_duplicate_user(self):
        """Test creating user with not unique email or username fails"""
        payload = {
            'email': 'test@email.com',
            'password': '123Testpassword',
        }
        create_user(**payload)
        resp = self.client.post(LIST_CREATE_USER_URL, payload)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that password should be more than 5 characters"""
        payload = {
            'email': 'test@email.com',
            'password': '123t',
        }
        resp = self.client.post(LIST_CREATE_USER_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(get_user_model().objects.filter(email=payload['email']).exists())
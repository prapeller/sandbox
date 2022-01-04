from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

LIST_CREATE_USER_URL = reverse('users:list-create')
TOKEN_URL = reverse('users:token')


def get_user_url(pk):
    return reverse('users:retrieve-update-destroy', kwargs={'pk': pk})


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

    def test_create_token_for_user(self):
        """Test that a token is created for the user"""
        payload = {'email': 'test@email.com', 'password': '123Testpass'}
        create_user(**payload)
        resp = self.client.post(TOKEN_URL, payload)

        self.assertIn('token', resp.data)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_create_token_invalid_credentials(self):
        """Test that a token is not created for the user if invalid credentials are given"""
        create_user(**{'email': 'test@email.com', 'password': '123Testpass'})
        payload = {'email': 'testosteron@email.com', 'password': '123Testpass'}
        resp = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', resp.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token is not created if user doesn't exist"""
        payload = {'email': 'test@email.com', 'password': '123Testpass'}
        resp = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', resp.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_missing_fields(self):
        """Test that token is not created if credentials are empty"""
        payload = {'email': 'test@email.com', 'password': ''}
        resp = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', resp.data)
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """Test that authenticatino is required for users"""
        user = create_user(**{'email': 'test@email.com', 'password': '123Testpass'})
        resp = self.client.get(get_user_url(user.pk))

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class AuthUserApiTest(TestCase):
    """Test API requests that require authentication"""

    def setUp(self) -> None:
        self.user = create_user(email='test@email.com', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.user_url = get_user_url(self.user.pk)

    def test_retrieve_profile_success(self):
        """Test retrieving profile for logged in user"""
        resp = self.client.get(self.user_url)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, {'id':self.user.pk, 'email': self.user.email})

    def test_post_to_profile_not_allowed(self):
        """Test that post to profile is not allowed via me url"""
        resp = self.client.post(self.user_url, {})

        self.assertEqual(resp.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        """Test updating the user profile for authenticated user"""
        payload = {'email': 'changed@email.com', 'password': 'changedpass'}
        resp = self.client.patch(self.user_url, payload)
        self.user.refresh_from_db()

        self.assertEqual(self.user.email, payload['email'])
        self.assertTrue(self.user.check_password, payload['password'])
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

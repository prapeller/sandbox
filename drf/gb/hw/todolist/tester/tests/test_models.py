from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

from rest_framework.authtoken.models import Token

from mixer.backend.django import mixer


class UserModelTests(TestCase):

    def test_create_user_without_username_successful(self):
        """test creating user without username is successful"""
        email = 'test@email.com'
        password = '123Testpassword'
        user = get_user_model().objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_email_successful(self):
        """test creating different users is successful
         creating user with existing email is unsuccessful"""
        mixer.blend(get_user_model())
        mixer.blend(get_user_model())

        email = 'test@email.com'
        password = '123Testpassword'
        get_user_model().objects.create_user(email=email, password=password)

        with self.assertRaises(IntegrityError):
            get_user_model().objects.create_user(email=email, password=password)

    def test_new_user_email_normalized(self):
        """test the email for a new user is normalized"""
        email = 'test@EmaIl.COM'
        user = get_user_model().objects.create_user(email, password='test')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='test')

    def test_create_new_superuser(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@test.com',
            password='test'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_anonymous_user(self):
        """test creating a new anonymous user and it has Token"""
        user = get_user_model().objects.create_anonymous_user()
        self.assertTrue(user.is_anonymous)
        self.assertIsNotNone(Token.objects.get(user=user))

from django.test import TestCase
from django.contrib.auth import get_user_model

from recipes.models import Tag, Ingredient
from handler.management.commands.create_sample_user import create_sample_user


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """test creating a new user with an email is successful"""
        email = 'test@email.com'
        password = '123Testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        self.assertFalse(user.is_anonymous)

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

    # def test_create_anonuser(self):
    #     """test creating a new anonymous user and it has Token"""
    #     user = get_user_model().objects.create_anonymous_user()
    #     self.assertTrue(user.is_anonimous)
    #     self.assertIsNotNone(Token.objects.get(user=user))

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = Tag.objects.create(
            user=create_sample_user(),
            name='Vegan',
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ing = Ingredient.objects.create(
            user=create_sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ing), ing.name)
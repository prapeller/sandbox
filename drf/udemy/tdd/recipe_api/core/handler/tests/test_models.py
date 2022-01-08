from unittest.mock import patch

from django.test import TestCase
from django.contrib.auth import get_user_model

from recipes.models import Tag, Ingredient, Recipe, recipe_image_file_path


def create_sample_user(email='test@email.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_recipe_str(self):
        """Test the recipe string representation"""
        rec = Recipe.objects.create(
            user=create_sample_user(),
            title='Scrambled cucumber',
            time_minutes=1.5,
            price=5.99,
        )

        self.assertEqual(str(rec), rec.title)

    @patch('uuid.uuid4')
    def test_recipe_filename_uuid(self, mock_uuid):
        """Test image is saved in the correct location"""
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid

        file_path = recipe_image_file_path(instance=None, filename='filename.jpg')
        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from handler.management.commands.create_sample_user import create_sample_user
from recipes.serializers import TagSerializer, IngredientSerializer
from recipes.models import Tag, Ingredient

TAGS_URL = reverse('recipes:tag-list')
INGREDIENT_URL = reverse('recipes:ingredient-list')


def sample_user(email='test@email.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class PublicTagsApiTest(APITestCase):
    """"Test not authenticated user tags API"""

    def test_login_required(self):
        """Test that login is required for retrieving tags"""
        resp = self.client.get(TAGS_URL)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

class PublicIngredientApiTest(APITestCase):
    """"Test not authenticated user ingredients API"""

    def test_login_required(self):
        """Test that login is required for listing ingredients"""
        resp = self.client.get(INGREDIENT_URL)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
    """Test authenticated user tags API"""

    def setUp(self) -> None:
        self.user = create_sample_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_tags(self):
        """Test listing tags"""
        Tag.objects.create(user=self.user, name='Vegan')
        Tag.objects.create(user=self.user, name='Desert')
        resp = self.client.get(TAGS_URL)

        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, serializer.data)

    def test_list_tags_limited_to_user(self):
        """Test that tags returned are for the authenticated user"""
        user = self.user
        user_tag = Tag.objects.create(user=user, name='Juicy')

        another_user = create_sample_user(email='another@email.com')
        another_tag = Tag.objects.create(user=another_user, name='Fruity')

        resp = self.client.get(TAGS_URL)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]['name'], user_tag.name)

    def test_create_tag_successful(self):
        payload = {'name': 'testtag'}
        self.client.post(TAGS_URL, payload)
        exists = Tag.objects.filter(name=payload['name'], user=self.user)

        self.assertTrue(exists)

    def test_create_tag_invalid(self):
        """"Test creating a new tag with invalid payload"""
        payload = {'name': ''}
        resp = self.client.post(TAGS_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)


class PrivateIngredientsApiTests(TestCase):
    """Test authenticated user ingredients API"""

    def setUp(self) -> None:
        self.user = create_sample_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_ingredients(self):
        """Test listing ingredients"""
        Ingredient.objects.create(user=self.user, name='testname')
        Ingredient.objects.create(user=self.user, name='testname2')
        resp = self.client.get(INGREDIENT_URL)

        ingredients = Ingredient.objects.all().order_by('-name')
        serializer = IngredientSerializer(ingredients, many=True)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, serializer.data)

    def test_list_ingredients_limited_to_user(self):
        """Test that ingredients returned are for the authenticated user"""
        user = self.user
        user_ing = Ingredient.objects.create(user=user, name='testname')

        another_user = create_sample_user(email='another@email.com')
        another_ing = Ingredient.objects.create(user=another_user, name='testname2')

        resp = self.client.get(INGREDIENT_URL)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]['name'], user_ing.name)

    def test_create_ing_successful(self):
        payload = {'name': 'testname'}
        self.client.post(INGREDIENT_URL, payload)
        exists = Ingredient.objects.filter(name=payload['name'], user=self.user)

        self.assertTrue(exists)

    def test_create_ing_invalid(self):
        """"Test creating a new ingredient with invalid payload"""
        payload = {'name': ''}
        resp = self.client.post(INGREDIENT_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
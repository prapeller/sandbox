from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from recipes.models import Tag, Ingredient, Recipe
from recipes.serializers import TagSerializer, IngredientSerializer, RecipeSerializer, RecipeDetailSerializer

TAGS_URL = reverse('recipes:tag-list')
INGREDIENTS_URL = reverse('recipes:ingredient-list')
RECIPES_URL = reverse('recipes:recipe-list')
def recipes_detail_url(pk):
    """Return recipe detail url"""
    return reverse('recipes:recipe-detail', kwargs={'pk': pk})


def create_sample_user(email='test@email.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


def create_sample_tag(user, name='tag name'):
    """Create and return a sample tag"""
    return Tag.objects.create(user=user, name=name)


def create_sample_ingredient(user, name='ingredient name'):
    """Create and return a sample ingredient"""
    return Ingredient.objects.create(user=user, name=name)


def create_sample_recipe(user, **kwargs):
    """Create a sample recipe"""
    defaults = {
        'title': 'test recipe title',
        'time_minutes': 10.5,
        'price': 2.99
    }
    defaults.update(kwargs)
    return Recipe.objects.create(user=user, **defaults)


class PublicApiTest(APITestCase):
    """"Test not authenticated user tags API
    Test not authenticated user ingredients API
    Test not authenticated user recipes API
    """

    def test_login_required_for_tags(self):
        """Test that login is required for retrieving tags"""
        resp = self.client.get(TAGS_URL)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_required_for_ingredients(self):
        """Test that login is required for listing ingredients"""
        resp = self.client.get(INGREDIENTS_URL)

        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_required_for_recipes(self):
        """Test that login is required for listing recipes"""
        resp = self.client.get(RECIPES_URL)

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
        resp = self.client.get(INGREDIENTS_URL)

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

        resp = self.client.get(INGREDIENTS_URL)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data[0]['name'], user_ing.name)

    def test_create_ing_successful(self):
        payload = {'name': 'testname'}
        self.client.post(INGREDIENTS_URL, payload)
        exists = Ingredient.objects.filter(name=payload['name'], user=self.user)

        self.assertTrue(exists)

    def test_create_ing_invalid(self):
        """"Test creating a new ingredient with invalid payload"""
        payload = {'name': ''}
        resp = self.client.post(INGREDIENTS_URL, payload)

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)


class PrivateRecipeApiTests(TestCase):
    """Test authenticated user recipes API"""

    def setUp(self) -> None:
        self.user = create_sample_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_list_recipes(self):
        """Test listing recipes"""
        rec_1 = create_sample_recipe(user=self.user)
        rec_2 = create_sample_recipe(user=self.user)
        resp = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data, serializer.data)

    def test_recipes_limited_to_user(self):
        """Test that recipes returned are for the authenticated user"""
        user = self.user
        user_rec = create_sample_recipe(user=user, title='testtitle')

        another_user = create_sample_user(email='another@email.com')
        another_user_rec = create_sample_recipe(user=another_user, title='testtitle2')

        resp = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 1)
        self.assertEqual(resp.data, serializer.data)
        self.assertEqual(resp.data[0]['title'], user_rec.title)

    def test_view_recipe_detail(self):
        """Test viewing a recipe """
        recipe = create_sample_recipe(user=self.user)
        recipe.tags.add(create_sample_tag(user=self.user))
        recipe.ingredients.add(create_sample_ingredient(user=self.user))

        url = recipes_detail_url(recipe.pk)
        resp = self.client.get(url)

        serializer = RecipeDetailSerializer(recipe)
        self.assertEqual(resp.data, serializer.data)


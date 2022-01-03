from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.urls import reverse

from rest_framework.test import APIClient, APITestCase
from rest_framework import status

from mixer.backend.django import mixer

from todo.models import Project, Todo

API_LIST_USER_URL = reverse('user-list')
API_LIST_PROJECT_URL = reverse('project-list')
API_LIST_TODO_URL = reverse('todo-list')


def create_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


class AnonymousUserApiTests(TestCase):
    """Test the anonymous (not authenticated) users API"""

    def setUp(self):
        self.client = APIClient()

    def test_anonusers_api_acess(self):
        """Test anonymous users forbidden access to list models"""
        resp = self.client.get(API_LIST_USER_URL)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        resp = self.client.get(API_LIST_PROJECT_URL)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        resp = self.client.get(API_LIST_TODO_URL)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)


class AuthUserApiTests(APITestCase):
    """Test the anonymous (not authenticated) users API"""

    def setUp(self):

        self.user_1 = create_user(email='test1@email.com', password='test')
        self.user_2 = create_user(email='test2@email.com', password='test')
        self.user_3 = create_user(email='test3@email.com', password='test')
        self.project_1 = mixer.blend(Project, users=(self.user_1, self.user_2))
        self.project_2 = mixer.blend(Project, users=(self.user_2, self.user_3))
        self.project_3 = mixer.blend(Project, users=(self.user_1, self.user_3))
        self.todo_1 = mixer.blend(Todo, creator=self.user_1, project=self.project_1)
        self.todo_2 = mixer.blend(Todo, creator=self.user_2, project=self.project_2)
        self.todo_3 = mixer.blend(Todo, creator=self.user_3, project=self.project_3)

    def test_auth_api_acess_list(self):
        """Test authenticated users granted access to list models"""
        self.client.force_login(self.user_1)

        resp = self.client.get(API_LIST_USER_URL)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        resp = self.client.get(API_LIST_PROJECT_URL)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        resp = self.client.get(API_LIST_TODO_URL)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_auth_api_acess_change(self):
        """Test authenticated and authorized users can change users/projects/todos"""
        CAN_CHANGE_USER = Permission.objects.get(codename='change_user')
        CAN_CHANGE_PROJECT = Permission.objects.get(codename='change_project')
        CAN_CHANGE_TODO = Permission.objects.get(codename='change_todo')

        API_USER_DETAIL_URL = reverse('user-detail', kwargs={'pk':self.user_2.pk})
        API_PROJECT_DETAIL_URL = reverse('project-detail', kwargs={'pk':self.project_1.pk})
        API_TODO_DETAIL_URL = reverse('todo-detail', kwargs={'pk':self.todo_1.pk})

        self.client.force_login(self.user_1)
        resp = self.client.patch(API_USER_DETAIL_URL, {'email': 'test@email.com'})
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        resp = self.client.patch(API_PROJECT_DETAIL_URL, {'name': 'test'})
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
        resp = self.client.patch(API_TODO_DETAIL_URL, {'text': 'test'})
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

        self.user_2.user_permissions.add(CAN_CHANGE_USER)
        self.user_2.user_permissions.add(CAN_CHANGE_PROJECT)
        self.user_2.user_permissions.add(CAN_CHANGE_TODO)
        self.client.force_login(self.user_2)
        resp = self.client.patch(API_USER_DETAIL_URL, {'email': 'test@email.com'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        resp = self.client.patch(API_PROJECT_DETAIL_URL, {'name': 'test'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        resp = self.client.patch(API_TODO_DETAIL_URL, {'text': 'test'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList

from collections import OrderedDict
from mixer.backend.django import mixer

from authors.models import Author
from authors.views import AuthorModelViewSet, BioModelViewSet, BookModelViewSet


class TestAuthorView(TestCase):

    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.client = APIClient()
        self.super_user = get_user_model().objects.create_superuser(
            username='superuser',
            email='test@email.com',
            password='testpass'
        )
        self.user = get_user_model().objects.create_user(
            username='user',
            email='test2@email.com',
            password='testpass'
        )
        self.staff = get_user_model().objects.create_user(
            username='staff',
            email='test3@email.com',
            password='testpass',
            is_staff=True
        )

    def test_modelviewset_authors_apifactory(self):
        """Test /api/modelviewset_authors/ endpoint using particular view
        superuser can create
        usual user cant read
        staff can read"""

        # runs every time for empty db (in this case its sqlite)
        # in order not to empty every time, test can run with arg --keepdb

        post_request = self.factory.post('/api/modelviewset_authors/',
                                         {
                                             'first_name': 'Sasha',
                                             'last_name': 'Pushkin',
                                             'birth_year': 1799
                                         },
                                         )
        force_authenticate(request=post_request, user=self.super_user)
        view = AuthorModelViewSet.as_view({'post': 'create', 'get': 'list'})
        a, b, resp = (view(post_request), view(post_request), view(post_request))
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.data['first_name'], 'Sasha')
        self.assertEqual(type(resp.data), ReturnDict)
        self.assertEqual(resp.data['id'], 3)

        get_request = self.factory.get('/api/modelviewset_authors/')
        force_authenticate(request=get_request, user=self.user)
        resp = view(get_request)
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

        force_authenticate(request=get_request, user=self.staff)
        resp = view(get_request)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(type(resp.data), ReturnList)
        self.assertEqual(len(resp.data), 3)

    def test_modelviewset_authors_apiclient(self):
        """Test /api/modelviewset_authors/ endpoint using client
        usual user and anonymous users can't read
        superuser can create
        staff can read"""
        payload = {'first_name': 'Sasha',
                   'last_name': 'Pushkin',
                   'birth_year': 1799}
        self.client.login(username='superuser', password='testpass')
        a, b, resp = (
            self.client.post('/api/modelviewset_authors/', payload),
            self.client.post('/api/modelviewset_authors/', payload),
            self.client.post('/api/modelviewset_authors/', payload)
        )
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        self.client.logout()
        resp = self.client.get('/api/modelviewset_authors/')
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username='user', password='testpass')
        resp = self.client.get('/api/modelviewset_authors/')
        self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)

        author = mixer.blend(Author)
        author = mixer.blend(Author)
        author = mixer.blend(Author)

        self.client.login(username='staff', password='testpass')
        resp = self.client.get('/api/modelviewset_authors/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 6)
        self.assertEqual(resp.data[5]['first_name'], author.first_name)

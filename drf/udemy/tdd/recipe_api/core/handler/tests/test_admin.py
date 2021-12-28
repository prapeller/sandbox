from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@test.com',
            password='test'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@test.com',
            password='test',
        )

    def test_users_list_page(self):
        """test that users are listed on user page"""
        url = reverse('admin:users_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.email)

    def test_users_change_page(self):
        """test that user change page works"""
        url = reverse('admin:users_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, self.user.email)

    def test_users_create_page(self):
        """test that user change page works"""
        url = reverse('admin:users_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'username')
        self.assertContains(res, 'password')

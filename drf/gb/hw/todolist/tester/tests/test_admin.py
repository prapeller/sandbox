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
        """test that user are listed on users page showing their email"""
        url = reverse('admin:users_user_changelist')
        resp = self.client.get(url)

        self.assertContains(resp, self.user.email)

    def test_users_change_page(self):
        """test that user change page works"""
        url = reverse('admin:users_user_change', args=[self.user.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.user.email)
        self.assertNotContains(resp, self.user.password)

    def test_users_create_page(self):
        """test that user add page works with all necessary fields"""
        url = reverse('admin:users_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Email:')
        self.assertContains(res, 'Username')
        self.assertContains(res, 'Password')
        self.assertContains(res, 'Password confirmation')
        self.assertContains(res, 'Active')
        self.assertContains(res, 'Staff status')
        self.assertContains(res, 'Superuser status')

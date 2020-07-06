from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status


class AdminSiteTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_super_user(
            email="admin@gmail.com",
            password="password1234  "
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@gmail.com",
            password="password",
            name="Testing User"
        )

    def test_users_listed(self):
        """Test that user are listed in user function """
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url, follow=True)
        print(f'Response is: {res}')

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """test that the user edit  page works"""
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

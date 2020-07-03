from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUserModel(TestCase):
    def test_create_user_with_email_successful(self):
        """ test creating a new user with email is succesfull"""
        email = "abedxh@gmail.com"
        password = "password"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Testing the email for new user is normaized"""

        email = "abed@GMAIL>COM"
        user = get_user_model().objects.create_user(email=email, password="1234")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test crating user with no valid email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password="1234")

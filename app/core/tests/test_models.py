from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with an email is successful"""
        email = 'test@recipe.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email of the user is normalized"""
        email = 'test@RECIPE.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='Password123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email_address(self):
        """Test create user with invalid email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='Password123'
            )


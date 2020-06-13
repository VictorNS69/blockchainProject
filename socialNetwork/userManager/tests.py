from django.test import TestCase
from django.contrib.auth.models import User
from .models import Users

# Create your tests here.

class UserModelTests(TestCase):

    def test_new_user(self):
        """Creating Users model"""
        auth_user = User.objects.create_user(username="danilo", email="", password="1234")
        Users.objects.create(user=auth_user, bytes="0x0")
        user_object = Users.objects.get(user=auth_user)
        self.assertEqual(user_object.bytes, "0x0")
        print(f"Test successful!")


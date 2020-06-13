from django.test import TestCase
from django.contrib.auth.models import User
from .models import Users


class UserModelTests(TestCase):

    def test_new_user(self):
        """Creating Users model"""
        user = User.objects.create_user(username="user1", email="test@test.com", password="1234")
        Users.objects.create(user=user, bytes="0xa1c2b8080ed4b6f56211e0295659ef87dd454b0a884198c10384f230525d4ee8")

        user_object = Users.objects.get(user=user)
        self.assertEqual(user_object.bytes, "0xa1c2b8080ed4b6f56211e0295659ef87dd454b0a884198c10384f230525d4ee8")


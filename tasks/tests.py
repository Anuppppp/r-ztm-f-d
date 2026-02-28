from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

class TaskTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="pass123"
        )
        self.client.login(username="test", password="pass123")

    def test_create_task(self):
        response = self.client.post("/api/tasks/", {
            "title": "Test Task"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
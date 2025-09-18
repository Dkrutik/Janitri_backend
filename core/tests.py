from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(APITestCase):
    def test_register_user(self):
        url = reverse("register")
        data = {"email": "test@example.com", "username": "testuser", "password": "testpass123"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

from django.test import TestCase
from django.urls import reverse

class SignupTestCase(TestCase):
    def test_signup(self):
        response = self.client.post(reverse('signup'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('message', response.json())

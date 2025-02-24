from django.test import TestCase
from django.urls import reverse

class MyWebsiteTests(TestCase):
    def test_homepage_loads(self):
        """Test if the homepage loads successfully"""
        response = self.client.get(reverse('index'))  # Change 'home' to your actual homepage URL name
        self.assertEqual(response.status_code, 200)  # 200 means success

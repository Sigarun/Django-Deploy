from django.test import TestCase
from django.urls import reverse

class TemplateTest(TestCase):

    def test_is_index_accessible(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

from django.urls import reverse
from django.test import TestCase


class ProfilesUrlsTestCase(TestCase):
    def setUp(self):
        pass

    def test_index(self):
        url = reverse("index")
        self.assertEqual(url, "/")

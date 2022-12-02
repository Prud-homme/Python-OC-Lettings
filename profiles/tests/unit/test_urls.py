from django.urls import reverse
from django.test import TestCase


class ProfilesUrlsTestCase(TestCase):
    def setUp(self):
        pass

    def test_index(self):
        url = reverse("profiles:index")
        self.assertEqual(url, "/profiles/")

    def test_profile(self):
        url = reverse("profiles:profile", args=[1])
        self.assertEqual(url, "/profiles/1/")

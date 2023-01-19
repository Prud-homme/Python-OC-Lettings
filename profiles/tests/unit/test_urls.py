from django.urls import reverse
from django.test import TestCase


class ProfilesUrlsTestCase(TestCase):
    def setUp(self):
        pass

    def test_index(self):
        url = reverse("profiles:index")
        self.assertEqual(url, "/profiles/")

    def test_profile(self):
        url = reverse("profiles:profile", args=["username"])
        self.assertEqual(url, "/profiles/username/")

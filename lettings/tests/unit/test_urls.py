from django.urls import reverse
from django.test import TestCase


class LettingsUrlsTestCase(TestCase):
    def setUp(self):
        pass

    def test_index(self):
        url = reverse("lettings:index")
        self.assertEqual(url, "/lettings/")

    def test_letting(self):
        url = reverse("lettings:letting", args=[1])
        self.assertEqual(url, "/lettings/1/")

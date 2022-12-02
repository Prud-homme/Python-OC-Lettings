from django.test import TestCase
from django.urls import reverse


class IndexViewTestCase(TestCase):
    def setUp(self):
        """
        GET request to main index and save response in a variable.
        """
        url = reverse("index")
        self.response = self.client.get(url)

    def test_index_template_name(self):
        """
        Test if the template are used is the correct.
        """
        self.assertTemplateUsed(self.response, "index.html")

    def test_index_template_content(self):
        """
        Test the content of html response
        """
        assert "<title>Holiday Homes</title>" in self.response.content.decode()
        assert self.response.status_code == 200

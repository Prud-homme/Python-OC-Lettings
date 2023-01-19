from django.test import TestCase
from django.urls import reverse


class IndexViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_index_template_name(self):
        """
        Test if the template are used is the correct.
        """
        url = reverse("index")
        response = self.client.get(url)

        assert response.status_code == 200
        self.assertTemplateUsed(response, "index.html")

    def test_index_template_content(self):
        """
        Test the content of html response
        """
        url = reverse("index")
        response = self.client.get(url)
        content = response.content.decode()

        assert response.status_code == 200
        assert "<title>Holiday Homes</title>" in content

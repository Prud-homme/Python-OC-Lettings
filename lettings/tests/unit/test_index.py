import pytest
from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db()
class IndexViewTestCase(TestCase):
    def setUp(self):
        """
        Create an address and a letting in the test database.
        """
        Address.objects.create(
            number=7217,
            street="Bedford Street",
            city="Brunswick",
            state="GA",
            zip_code=31525,
            country_iso_code="USA",
        )
        self.address = Address.objects.all().first()
        Letting.objects.create(
            title="Joshua Tree Green Haus /w Hot Tub", address=self.address
        )
        self.letting = Letting.objects.all().first()

    def test_index_template_name(self):
        """
        Test if the template are used is the correct.
        """
        url = reverse("lettings:index")
        response = self.client.get(url)

        assert response.status_code == 200
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_index_template_content(self):
        """
        Test the content of html response
        """
        url = reverse("lettings:index")
        response = self.client.get(url)
        content = response.content.decode()

        assert response.status_code == 200
        assert "<title>Lettings</title>" in content
        assert self.letting.title in content

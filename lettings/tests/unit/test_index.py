import pytest
from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db()
class IndexViewTestCase(TestCase):
    def setUp(self):
        """
        Create an address and a letting in the test database.
        GET request to index lettings and save response in a variable.
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
        url = reverse("lettings:index")
        self.response = self.client.get(url)

    def test_index_template_name(self):
        """
        Test if the template are used is the correct.
        """
        self.assertTemplateUsed(self.response, "lettings/index.html")

    def test_index_template_content(self):
        """
        Test if the title of letting previously created are in the content of html response
        """
        self.assertInHTML(self.letting.title, self.response.content.decode())

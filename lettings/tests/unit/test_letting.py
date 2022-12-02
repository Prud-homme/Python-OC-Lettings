import pytest
from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.mark.django_db()
class LettingViewTestCase(TestCase):
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
        url = reverse("lettings:letting", args=[1])
        self.response = self.client.get(url)

    def test_index_template_name(self):
        """
        Test if the template are used is the correct.
        """
        self.assertTemplateUsed(self.response, "lettings/letting.html")

    def test_index_template_content(self):
        """
        Test the content of html response
        """
        assert f"<title>{self.letting.title}</title>"
        assert self.letting.address.__str__() in self.response.content.decode()
        assert self.letting.address.city in self.response.content.decode()
        assert self.letting.address.state in self.response.content.decode()
        assert str(self.letting.address.zip_code) in self.response.content.decode()
        assert self.letting.address.country_iso_code in self.response.content.decode()
        assert self.response.status_code == 200

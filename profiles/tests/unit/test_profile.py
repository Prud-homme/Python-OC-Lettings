import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from profiles.models import Profile


@pytest.mark.django_db()
class ProfileViewTestCase(TestCase):
    def setUp(self):
        """
        Create an user and a profile in the test database.
        """
        self.user = User.objects.create_user(
            username="test_user", password="?2.PabY8MB"
        )
        Profile.objects.create(user=self.user, favorite_city="Paris")
        self.profile = Profile.objects.all().first()

    def test_index_template_name(self):
        """
        Test if the template are used is the correct.
        """
        url = reverse("profiles:profile", args=[self.user.username])

        response = self.client.get(url)
        content = response.content.decode()

        assert response.status_code == 200
        self.assertTemplateUsed(response, "profiles/profile.html")

    def test_index_template_content(self):
        """
        Test if the title of letting previously created are in the content of html response
        """
        url = reverse("profiles:profile", args=[self.user.username])
        response = self.client.get(url)
        content = response.content.decode()

        assert response.status_code == 200
        assert f"<title>{self.profile.user.username}</title>" in content
        assert self.profile.favorite_city in content

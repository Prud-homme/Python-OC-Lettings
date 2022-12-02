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
        GET request to index of profiles and save response in a variable.
        """
        username = "test_user"
        password = "?2.PabY8MB"
        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, favorite_city="Paris")
        self.profile = Profile.objects.all().first()
        url = reverse("profiles:profile", args=[username])
        self.response = self.client.get(url)

    def test_index_template_name(self):
        """
        Test if the template are used is the correct.
        """
        self.assertTemplateUsed(self.response, "profiles/profile.html")

    def test_index_template_content(self):
        """
        Test if the title of letting previously created are in the content of html response
        """
        assert self.profile.user.username in self.response.content.decode()
        assert self.profile.favorite_city in self.response.content.decode()

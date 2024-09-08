from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        """
        Set up a test user and profile for testing the Profile model.
        """
        self.user = User.objects.create(username="testuser")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profile_creation(self):
        """
        Test that a Profile object is created and linked to a User object.
        """
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(self.profile.favorite_city, "Paris")

    def test_profile_str_method(self):
        """
        Test the __str__ method of the Profile model returns the username.
        """
        self.assertEqual(str(self.profile), "testuser")

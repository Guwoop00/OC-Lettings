from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileViewsTest(TestCase):

    def setUp(self):
        """
        Set up a test user and profile for testing views.
        """
        self.user = User.objects.create(username="testuser")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_index_view(self):
        """
        Test the index view returns the correct template and context.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertIn(self.profile, response.context['profiles_list'])

    def test_profile_view(self):
        """
        Test the profile view returns the correct template and context for a specific user.
        """
        response = self.client.get(reverse('profiles:profile', kwargs={'username': self.user.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertEqual(response.context['profile'], self.profile)

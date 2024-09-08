from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import index, profile


class ProfileUrlsTest(SimpleTestCase):

    def test_index_url_resolves(self):
        """
        Test that the URL for the index view resolves to the correct view function.
        """
        url = reverse('profiles:index')
        self.assertEqual(resolve(url).func, index)

    def test_profile_url_resolves(self):
        """
        Test that the URL for the profile view resolves to the correct view function.
        """
        url = reverse('profiles:profile', kwargs={'username': 'testuser'})
        self.assertEqual(resolve(url).func, profile)

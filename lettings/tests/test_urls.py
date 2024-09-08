from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class URLTests(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street='Main Street',
            city='Anytown',
            state='CA',
            zip_code=12345,
            country_iso_code='USA'
        )
        self.letting = Letting.objects.create(
            title='Beautiful Apartment',
            address=self.address
        )

    def test_index_url(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')
        # import pdb;pdb.set_trace()
        self.assertIn('<title>Lettings</title>', str(response.content))

    def test_letting_url(self):
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'letting.html')
        self.assertContains(response, self.letting.title)
        self.assertContains(response, self.letting.address.street)

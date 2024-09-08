from django.test import TestCase
from lettings.models import Address, Letting


class AddressModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street='Main Street',
            city='Anytown',
            state='CA',
            zip_code=12345,
            country_iso_code='USA'
        )

    def test_address_str(self):
        self.assertEqual(str(self.address), '123 Main Street')

    def test_address_fields(self):
        self.assertEqual(self.address.number, 123)
        self.assertEqual(self.address.street, 'Main Street')
        self.assertEqual(self.address.city, 'Anytown')
        self.assertEqual(self.address.state, 'CA')
        self.assertEqual(self.address.zip_code, 12345)
        self.assertEqual(self.address.country_iso_code, 'USA')


class LettingModelTest(TestCase):
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

    def test_letting_str(self):
        self.assertEqual(str(self.letting), 'Beautiful Apartment')

    def test_letting_fields(self):
        self.assertEqual(self.letting.title, 'Beautiful Apartment')
        self.assertEqual(self.letting.address, self.address)

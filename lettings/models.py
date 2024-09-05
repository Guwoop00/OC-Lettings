from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    This class represents a physical address.

    Attributes:
        number (int): The street number of the address.
        street (str): The name of the street.
        city (str): The city in which the address is located.
        state (str): The state or region of the address, represented as a two-letter code.
        zip_code (int): The postal code of the address.
        country_iso_code (str): The ISO 3166-1 alpha-3 code of the country.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    This class represents a letting (rental property) that has an associated address.

    Attributes:
        title (str): The title or name of the letting.
        address (Address): The address associated with the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

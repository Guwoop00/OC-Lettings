from django.contrib import admin

from lettings.models import Letting, Address
from profiles.models import Profile

# Registers the Letting model with the Django admin site.

admin.site.register(Letting)
"""
Register the Letting model with the Django admin site.

This allows the Letting model to be managed through the Django admin interface.
"""

# Registers the Address model with the Django admin site.

admin.site.register(Address)
"""
Register the Address model with the Django admin site.

This allows the Address model to be managed through the Django admin interface.
"""

# Registers the Profile model with the Django admin site.

admin.site.register(Profile)
"""
Register the Profile model with the Django admin site.

This allows the Profile model to be managed through the Django admin interface.
"""

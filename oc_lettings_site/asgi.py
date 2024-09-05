import os

from django.core.asgi import get_asgi_application

# Set the default settings module for the 'oc_lettings_site' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

"""
ASGI application callable for the 'oc_lettings_site' project.

This is used by ASGI servers to communicate with the Django application.
It is set up using the settings defined in 'oc_lettings_site.settings'.
"""

application = get_asgi_application()

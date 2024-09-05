import os

from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'oc_lettings_site' project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')

"""
WSGI application callable for the 'oc_lettings_site' project.

This is used by WSGI servers to communicate with the Django application.
It is set up using the settings defined in 'oc_lettings_site.settings'.
"""

application = get_wsgi_application()

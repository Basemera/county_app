"""
WSGI config for country_app_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'country_app_project.settings')
project_folder = os.path.expanduser('~/Documents/python/country/county_app/')
load_dotenv(os.path.join(project_folder, '.env'))

application = get_wsgi_application()

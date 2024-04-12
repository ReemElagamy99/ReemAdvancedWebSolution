"""
WSGI config for reemelagamyadvancedwebsolutions project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
#we usually don't use this folder

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reemelagamyadvancedwebsolutions.settings')

application = get_wsgi_application()

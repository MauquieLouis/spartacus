"""
WSGI config for spartacus project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/spartacus/spartacus')
sys.path.append('/home/spartacus/spartacus/spartacus')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spartacus.settings')

application = get_wsgi_application()

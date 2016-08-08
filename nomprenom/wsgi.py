"""
WSGI config for nomprenom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
import site
from django.core.wsgi import get_wsgi_application

site.addsitedir('/home/sushinski/virtualenvs/npn/npnenv/lib/python3.5/site-packages')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

activate_env=os.path.expanduser("/home/sushinski/virtualenvs/npnenv/bin/activate_this.py")
exec(open(activate_env).read())

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nomprenom.settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

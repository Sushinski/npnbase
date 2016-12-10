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

if os.path.exists("/home/sushinski/virtualenvs/npn/npnenv/bin/"):
    activate_env = os.path.expanduser("/home/sushinski/virtualenvs/npn/npnenv/bin/activate_this.py")
    exec(open(activate_env).read())
else:
    w_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../npnenv/Scripts"))
    if os.path.exists(w_path):
        activate_env = os.path.join(w_path, "activate_this.py")
        exec(open(activate_env).read())

os.environ["DJANGO_SETTINGS_MODULE"] = "nomprenom.settings"

application = get_wsgi_application()

"""Used for PythonAnywhere deployment."""
import os
import sys
import django
from django.core.wsgi import get_wsgi_application

path = '/home/djangoBasics/django-template/app'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

django.setup()
application = get_wsgi_application()

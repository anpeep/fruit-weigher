# fruitweigher/wsgi.py
import sys
import os
from django.core.wsgi import get_wsgi_application

# Ensure the 'src' directory is in the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fruitweigher.settings')

application = get_wsgi_application()

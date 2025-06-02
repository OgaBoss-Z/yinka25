from whitenoise import WhiteNoise
import os

from django.core.asgi import get_asgi_application

application = WhiteNoise(application, root='media/', prefix='media/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yinka.settings')

application = get_asgi_application()

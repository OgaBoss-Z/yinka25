import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yinka.settings')
django.setup()

User = get_user_model()

username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'yinkaAdmin')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'yinkakayode25@gmail.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'yinka@co2025')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superuser {username} created.')
else:
    print(f'Superuser {username} already exists.')

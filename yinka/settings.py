import os
from pathlib import Path
import dj_database_url

print("DEBUG:", os.getenv("DEBUG"))
print("RENDER:", os.getenv("RENDER"))

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Environment
RENDER = os.getenv('RENDER', "False") == 'True'
DEBUG = os.getenv("DEBUG", "True") == "True"

# Secret key
#SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-for-dev-only")
SECRET_KEY = 'django-insecure-2tp-js_wt#72iyq5pw266&qrann4!7)hxoc-@z_n7df$#u05jr'

# Allowed hosts
ALLOWED_HOSTS = ['*']  # You can restrict this in production

# Installed apps
INSTALLED_APPS = [
    'web.apps.WebConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'cloudinary',
    'cloudinary_storage',
]

# CKEditor config
CKEDITOR_UPLOAD_PATH = "uploads/"

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLs and WSGI
ROOT_URLCONF = 'yinka.urls'
WSGI_APPLICATION = 'yinka.wsgi.application'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'yinka.context_processor.current_year',
            ],
        },
    },
]

# Database: use SQLite locally, PostgreSQL in production
if RENDER:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True

# Static files
# STATIC
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# MEDIA
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Detect production via RENDER environment variable
IS_RENDER = os.getenv("RENDER", "").lower() == "true"

if IS_RENDER:
    print("🔵 Cloudinary config is active.")
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
        'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
        'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
    }
else:
    print("🟢 Local file system storage is active.")
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Primary key type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

print("Using Cloudinary for media storage:", os.getenv("RENDER", "False") == "True")

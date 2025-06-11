import os
from pathlib import Path
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# === BASE DIRECTORY ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === ENVIRONMENT DETECTION ===
RENDER_ENV = os.getenv('RENDER', '').lower() == 'true'
DEBUG = not RENDER_ENV  # False in production

print("🔍 RENDER_ENV:", RENDER_ENV)
print("🔍 DEBUG:", DEBUG)

# === SECRET KEY ===
SECRET_KEY = 'django-insecure-2tp-js_wt#72iyq5pw266&qrann4!7)hxoc-@z_n7df$#u05jr'

# === ALLOWED HOSTS ===
ALLOWED_HOSTS = ['*']  # 

# === INSTALLED APPS ===
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

# === MIDDLEWARE ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# === URL & WSGI ===
ROOT_URLCONF = 'yinka.urls'
WSGI_APPLICATION = 'yinka.wsgi.application'

# === TEMPLATES ===
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

# === DATABASES ===
if RENDER_ENV:
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

# === PASSWORD VALIDATION ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === INTERNATIONALIZATION ===
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Lagos'
USE_I18N = True
USE_TZ = True

# === STATIC FILES ===
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# === CKEDITOR CONFIG ===
CKEDITOR_UPLOAD_PATH = "uploads/"

# === MEDIA FILE STORAGE ===
if RENDER_ENV:
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
        "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
        "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
    }
    print("✅ Using Cloudinary for media storage.")
else:
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    print("📁 Using local file storage.")

# === PRIMARY KEY ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

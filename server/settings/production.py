from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['https://wwww.example.com.mx']

# Config db using MySQL
DATABASES = {
        'default': {
            'ENGINE': config('DATABASE_ENGINE'),
            'NAME': config('DATABASE_NAME'),
            'USER': config('DATABASE_USER'),
            'PASSWORD': config('DATABASE_PASSWORD'),
            'HOST': config('DATABASE_HOST', default='localhost'),
            'PORT': config('PORT'),
        }
    }

# Add MEDIA_URL and MEDIA_ROOT
MEDIA_URL=config('MEDIA_URL', default="/uploads/")
MEDIA_ROOT=config('MEDIA_ROOT', default="./uploads/")
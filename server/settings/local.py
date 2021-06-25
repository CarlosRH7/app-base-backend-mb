from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Config db using MySQL
DATABASES = {
        'default': {
            'ENGINE': config('DATABASE_ENGINE_LOCAL'),
            'NAME': config('DATABASE_NAME_LOCAL'),
            'USER': config('DATABASE_USER_LOCAL'),
            'PASSWORD': config('DATABASE_PASSWORD_LOCAL'),
            'HOST': config('DATABASE_HOST_LOCAL', default='localhost'),
            'PORT': config('PORT_LOCAL'),
        }
    }

# Add MEDIA_URL and MEDIA_ROOT
MEDIA_URL=config('MEDIA_URL_LOCAL', default="/uploads/")
MEDIA_ROOT=config('MEDIA_ROOT_LOCAL', default="./uploads/")
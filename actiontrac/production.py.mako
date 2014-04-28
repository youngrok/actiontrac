from settings import *

DEBUG = False
TEMPLATE_DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '${mysql_database}',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '${mysql_user}',
        'PASSWORD': '${mysql_password}',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

STATIC_ROOT = '${django_static_root}'

ALLOWED_HOSTS = ['*']

SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''

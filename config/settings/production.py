"""
Production settings

- 
"""

# import
# ------------------------------------------------------------------------------
from .base import *  # noqa
import os
# ------------------------------------------------------------------------------
# /import

# ENV
# ------------------------------------------------------------------------------
ENV_FILE = str(ENV_DIR + '/production')
env.read_env(ENV_FILE)
# ------------------------------------------------------------------------------
# /ENV

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = False
TEMPLATES['OPTIONS']['debug'] = DEBUG
# ------------------------------------------------------------------------------
# /DEBUG

# SECRET KEY
# ------------------------------------------------------------------------------
#SECRET_KEY = os.environ["SECRET_KEY"]
SECRET_KEY = env('DJANGO_SECRET_KEY')
# ------------------------------------------------------------------------------
# /SECRET KEY

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
ADMINS = (
    ('Bruno Santeramo', 'bruno.santeramo@gmail.com'),
)

MANAGERS = ADMINS
# ------------------------------------------------------------------------------
# /MANAGER CONFIGURATION

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'cashflow',
        'NAME': env('DB_NAME'),
        #'USER': os.environ['DB_USER'],
        'USER': env('DB_USER'),
        #'PASSWORD': os.environ.get('DB_PASSWORD', ''),
        'PASSWORD': env('DB_PASSWORD', ''),
        #'HOST': os.environ.get('DB_HOST', ''),
        'HOST': env('DB_HOST', ''),
        'PORT': '',
    }
}
# ------------------------------------------------------------------------------
# /DATABASE CONFIGURATION

# PASSWORD VALIDATION
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
# ------------------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------

# Some really nice defaults
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

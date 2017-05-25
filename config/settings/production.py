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
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
# ------------------------------------------------------------------------------
# /DEBUG

# SECRET KEY
# ------------------------------------------------------------------------------
#SECRET_KEY = os.environ["SECRET_KEY"]
SECRET_KEY = env('DJANGO_SECRET_KEY')
# ------------------------------------------------------------------------------
# /SECRET KEY

# ALLOWED HOSTS
# ------------------------------------------------------------------------------
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
# ------------------------------------------------------------------------------
# /ALLOWED HOSTS

# WSGI HANDLER
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('gunicorn', )
# ------------------------------------------------------------------------------
# /WSGI HANDLER

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
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
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
# ------------------------------------------------------------------------------
# /PASSWORD VALIDATION

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------

# Some really nice defaults
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# ------------------------------------------------------------------------------ 
# /AUTHENTICATION CONFIGURATION 
 
# EMAIL 
# ------------------------------------------------------------------------------ 
INSTALLED_APPS += ("anymail", ) 
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL', 
                         default='example <noreply@example.com>') 
SERVER_EMAIL = env('DJANGO_SERVER_EMAIL', default=DEFAULT_FROM_EMAIL) 
EMAIL_SUBJECT_PREFIX = env('DJANGO_EMAIL_SUBJECT_PREFIX', default='[example] ') 
 
EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"  # or sendgrid.EmailBackend, or... 
 
# Anymail with Mailgun 
ANYMAIL = { 
    "MAILGUN_API_KEY": env('DJANGO_MAILGUN_API_KEY'), 
    "MAILGUN_SENDER_DOMAIN": env('DJANGO_MAILGUN_SENDER_DOMAIN') 
} 
# ------------------------------------------------------------------------------ 
# /EMAIL 

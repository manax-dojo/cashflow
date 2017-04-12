"""
Django settings for cashflow project.
For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import environ
import os
import sys

from django.utils.translation import ugettext_lazy as _

# PATH vars
# ------------------------------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
root = lambda *x: os.path.join(ROOT_DIR, *x) 
BASE_DIR = root('cashflow') 
base = lambda *x: os.path.join(BASE_DIR, *x) 
APPS_DIR = root('apps') 
ENV_DIR = root('env')

sys.path.append(APPS_DIR) 

env = environ.Env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'CHANGE THIS!!!'

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)
#IN_TESTING = sys.argv[1:2] == ['test']

ALLOWED_HOSTS = []

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)
THIRD_PARTY_APPS = (
    'allauth',  # registration
    'allauth.account',  # registration
    'allauth.socialaccount',  # registration
    'avatar', # avatar 
    'crispy_forms', 
)


# Apps specific for this project go here.
LOCAL_APPS = (
    # Your stuff: custom apps go here
    'manax_theme_alpha.apps.ManaxThemeAlphaConfig',
    'users.apps.UsersConfig',
    'homepage.apps.HomepageConfig',
    'cashfield.apps.CashfieldConfig',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'config.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'config.wsgi.application'

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cashflow',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# Internationalization

LANGUAGE_CODE = 'en'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('en', _('English')),
    ('it', _('Italian')),
)

LOCALE_PATHS = (
    root('locale'),
)

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'


# MEDIA CONFIGURATION 
# ------------------------------------------------------------------------------ 
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root 

MEDIA_ROOT = root('media') 
 
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url 
MEDIA_URL = '/media/' 


# crispy-forms 
 
CRISPY_TEMPLATE_PACK = 'bootstrap3'  


# Additional locations of static files

STATICFILES_DIRS = [
    base('assets'),
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            base('templates'),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request', 
            ],
        },
    }
]

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth` 
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail 
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'optional'

ACCOUNT_ALLOW_REGISTRATION = env.bool('DJANGO_ACCOUNT_ALLOW_REGISTRATION', True)
ACCOUNT_ADAPTER = 'users.adapters.AccountAdapter'
SOCIALACCOUNT_ADAPTER = 'users.adapters.SocialAccountAdapter'

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = 'users.User'
#LOGIN_REDIRECT_URL = 'users:redirect'
LOGIN_REDIRECT_URL = 'cashfield:home'
LOGIN_URL = 'users:account_login' 

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r'^admin/'


# AVATAR CONFIGURATION
# ------------------------------------------------------------------------------
AVATAR_ADD_TEMPLATE = 'users/avatar/add.html'
AVATAR_CHANGE_TEMPLATE = 'users/avatar/change.html'
AVATAR_DELETE_TEMPLATE = 'users/avatar/confirm_delete.html'


# Your common stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------

# .currency.py for currency related settings
try:
    from .currency import *  # noqa
except ImportError:
    pass

# .local.py overrides all the common settings.
try:
    from .local import *  # noqa
except ImportError:
    pass


# importing test settings file if necessary
if IN_TESTING:
    from .testing import *  # noqa

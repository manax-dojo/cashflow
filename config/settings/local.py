"""
Local settings

- Run in Debug mode
- Add Django Debug Toolbar
- Add django-extensions as app
"""

# import
# ------------------------------------------------------------------------------
from .base import *  # noqa
# ------------------------------------------------------------------------------
# /import

# ENV
# ------------------------------------------------------------------------------
ENV_FILE = str(ENV_DIR + '/local')
env.read_env(ENV_FILE)
# ------------------------------------------------------------------------------
# /ENV

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
IN_TESTING = env.bool('IN_TESTING', default=False)
# ------------------------------------------------------------------------------
# /DEBUG


# django-debug-toolbar
# ------------------------------------------------------------------------------
MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]
# tricks to have debug toolbar when developing with docker
if os.environ.get('USE_DOCKER') == 'yes':
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += [ip[:-1] + "1"]

DEBUG_TOOLBAR_CONFIG = {
    'DISABLE_PANELS': [
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ],
    'SHOW_TEMPLATE_CONTEXT': True,
}

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Bruno Santeramo', 'bruno.santeramo@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# ------------------------------------------------------------------------------
# /MANAGER CONFIGURATION


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cashflow',
        'USER': 'cashflow',
        'PASSWORD': 'cashflow',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# You might want to use sqlite3 for testing in local as it's much faster.
if IN_TESTING:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/cashflow_test.db',
        }
    }
# ------------------------------------------------------------------------------
# /DATABASE CONFIGURATION

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )

# Your common stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------


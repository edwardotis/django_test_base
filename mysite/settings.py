# coding=utf-8
# Django settings for mysite project.
import os
import sys

import dj_database_url




# Normally you should not import ANYTHING from Django directly
# into your settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


PROJECT_ROOT = os.path.abspath(os.path.dirname(__name__))  # this is not Django setting.
print 'PROJECT_ROOT: %s' % PROJECT_ROOT

SITE_ROOT = os.path.dirname(__file__)  # this is not Django setting.
print 'SITE_ROOT: %s' % SITE_ROOT

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# DO NOT CHANGE ATOMIC_REQUESTS SETTING
ATOMIC_REQUESTS = False

ADMINS = (
    # ('Ed Johnson', 'ed@hiplead.com'),
)

MANAGERS = ADMINS
LOGIN_URL = '/accounts/login/'

# You must set environment variable int his format for default database connectivity
# DATABASE_URL = postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASES = {'default': dj_database_url.config()}

TEST_CHARSET = 'UTF8'

# Configure required ssl for heroku production dynos
# https://github.com/rdegges/django-sslify/issues/1
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# disable ssl requirement on localhost or if DEBUG enabled
SSLIFY_DISABLE = True if not 'DYNO' in os.environ else False
SSLIFY_DISABLE = True if DEBUG is True else SSLIFY_DISABLE

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# Allow all host headers
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = ''

# A site and 0 or more apps are contained within a django project.
PROJECT_DIR = os.path.abspath(os.path.dirname(__name__))  # this is not Django setting.
SITE_DIR = os.path.dirname(__file__)  # this is not Django setting.

# STATIC FILES ON HEROKU
#https://devcenter.heroku.com/articles/django-assets

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, 'collectedstaticfiles')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files

STATIC_PATH = os.path.join(SITE_DIR, 'static')  # aka os.path.join(PROJECT_DIR, 'donscraper', 'static')
STATIC_PATH2 = os.path.join(PROJECT_DIR, 'polls', 'static')
STATIC_PATH3 = os.path.join(PROJECT_DIR, 'addressbook', 'static')

# Additional locations of static files
STATICFILES_DIRS = (
    STATIC_PATH,
    STATIC_PATH2,
    STATIC_PATH3,
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'kfz5%%-vi69-a+rx*0wu+bab1)v4@x-^bgx-63g3pbtbc*ad1b'

# List of callables that know how to import mysite.templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # require SSL on all non-dev environments.
    'sslify.middleware.SSLifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mysite.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/mysite.templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),

    # NOTE, Relative path's work, but the dot notation did *not* work
    # os.path.join(os.path.dirname(__file__), '../mysite.templates'),

    # NOTE This would work if we wanted templates dir to live under myproject instead of mysites
    #os.path.join(os.path.dirname(__file__), '../templates'),

)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'registration',
    'polls',
    'addressbook',
    'south',
)

# http://stackoverflow.com/questions/9566676/django-debug-toolbar-in-heroku
if DEBUG is True:
    INSTALLED_APPS += (
        'debug_toolbar',
    )

#http://django-debug-toolbar.readthedocs.org/en/1.0/installation.html#explicit-setup

DEBUG_TOOLBAR_PATCH_SETTINGS = False

INTERNAL_IPS = ('127.0.0.1', )
if DEBUG is True:
    class AllIPS(list):
        def __contains__(self, item):
            return True

    INTERNAL_IPS = AllIPS()

print( 'DEBUG=%s' % DEBUG)
print( 'INTERNAL_IPS=%s' % INTERNAL_IPS)

# django-registration
# http://devdoodles.wordpress.com/2009/02/16/user-authentication-with-django-registration/
# https://bitbucket.org/devdoodles/registration_templates/downloads

# set a dummy email backend for development
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
# EMAIL_HOST = 'localhost'
#DEFAULT_FROM_EMAIL = 'webmaster@localhost'
#LOGIN_REDIRECT_URL = '/'
ACCOUNT_ACTIVATION_DAYS = 2  # One-week activation window; you may, of course, use a different value.

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': (u'%(asctime)s [%(process)d] [%(levelname)s] ' +
                       '%(name)s.%(funcName)s::%(lineno)s '
                       '%(message)s'),
        },
        'simple': {
            'format': u'%(levelname)s %(message)s'
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'mysite': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'polls': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'addressbook': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        }
    }
}

SOUTH_TESTS_MIGRATE = False  # To disable migrations and use syncdb instead

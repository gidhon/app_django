# Django settings for this project.

# forge absolute directory path

import os
PATH = os.path.dirname(__file__)

# continue default settings

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Gideon Kreitzer', 'admin@email.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'example',                                  # Or path to database file if using sqlite3.
        'USER': 'gideon',                                   # Not used with sqlite3.
        'PASSWORD': 'kubvp985hae5igubn',                    # Not used with sqlite3.
        'HOST': '',                                         # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                         # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Africa/Johannesburg'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-za'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '{}/../media'.format(PATH)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'http://example.com/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/cygnul/apps/example_com/site_static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    '{}/../static'.format(PATH),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+i8e)-d7zor9-#*v_ilmby%-dlea!ym6e6rc0&amp;='

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'bookingza.wsgi.application'

TEMPLATE_DIRS = (
    '{}/../static/templates'.format(PATH),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'south',
    'tinymce',
    'captcha',

    'base',
    'promotions',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#---------------------------------------#  ADDITIONAL CONFIG  #---------------------------------------#


# email section

EMAIL_HOST = 'smtp.example.com'
EMAIL_HOST_USER = 'gideon'
EMAIL_HOST_PASSWORD = 'ck7;TW+N~RxBsw5McNxz'
DEFAULT_FROM_EMAIL = 'Example.com <bookings@example.com>'

# Default: 'root@localhost' - email address that error messages come from, such as those sent to ADMINS and MANAGERS.
SERVER_EMAIL = 'server@example.com'

# Default: 25
EMAIL_PORT = 25


# email client validation

RECAPTCHA_PUBLIC_KEY = '6LculNsSA3AAAAGhR46vMGDDxQI2o_BvA'
RECAPTCHA_PRIVATE_KEY = '6LculNsSAAAAALbaczuYW7ow-gPqjkZV'


# log django-tinymce options

TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "paste, autosave, autoresize, save, fullscreen",
    'theme_advanced_buttons2_add': "separator, fullscreen",
    'theme_advanced_buttons3_add': "pastetext, pasteword, selectall, separator, save, cancel",
    'theme_advanced_blockformats': "p,h3,h4",
    'save_enablewhendirty': True,
    'custom_undo_redo_levels': 10,
    'schema': "html5",
}
TINYMCE_SPELLCHECKER = False

# custom global contexts

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += ('app.contexts.latest',)

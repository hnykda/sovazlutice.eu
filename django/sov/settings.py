"""
Django settings for sov project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'


SECRET_KEY = open("/var/www/dan/sovazlutice/secret_key.txt").read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


ALLOWED_HOSTS = ['sovazlutice.eu',
             'www.sovazlutice.eu']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'easy_thumbnails',
    'blog',
    'relic',
    'ways',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'django.core.context_processors.static',
  'django.core.context_processors.media',
  'cont_proces.extra_context',
)

ROOT_URLCONF = 'sov.urls'

WSGI_APPLICATION = 'sov.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'cs-cz'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

THUMBNAIL_ALIASES = {
    '': {
        'galRelThum': {'size': (384, 512), 'crop': True},
        'small': {'size': (100, 100)},
        'portf': {'size': (384, 512), 'crop': True},
        'nivoSlider': {'size': (600, 600), 'crop': True},
        'blogpost': {'size': (560, 300), 'crop': True},
        'post': {'size': (560, 300)},
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "sfiles"), )

# Templates
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

#SUMMERNOTE_CONFIG = {
#    'lang' : 'cs-CZ',
#}

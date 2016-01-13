# Django settings for moscowdjango project.
import os

from django import VERSION as DJANGO_VERSION

ROOT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

BOWER_COMPONENTS_ROOT = os.path.abspath(os.path.join(ROOT_PATH, 'components'))

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS
TIME_ZONE = 'Asia/Novosibirsk'
LANGUAGE_CODE = 'ru-ru'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(ROOT_PATH, 'gen_static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(ROOT_PATH, 'static'),
    os.path.join(ROOT_PATH, 'apps', 'theme', 'static'),
    os.path.join(ROOT_PATH, 'apps', 'blog_theme', 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.request',
                'apps.meetup.context.menu',
                'apps.meetup.context.all_events_processor',
                "django.template.context_processors.tz",
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'zinnia.context_processors.version',  # Optional
                "mezzanine.conf.context_processors.settings",
                "mezzanine.pages.context_processors.page",
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            "builtins": [
                "mezzanine.template.loader_tags",
            ],
        }
    }
]

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',

    "mezzanine.core.middleware.UpdateCacheMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    # Uncomment if using internationalisation or localisation
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",

)

AUTHENTICATION_BACKENDS = (
    #    'admin_sso.auth.DjangoSSOAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
    "mezzanine.core.auth_backends.MezzanineBackend",
)

ROOT_URLCONF = 'project.urls'

WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = ('',)

INSTALLED_APPS = (
    # 'suit',

    'apps.blog_theme',
    # 'apps.theme',
    "mezzanine_pagedown",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    "django.contrib.redirects",
    "django.contrib.sitemaps",

    'djangobower',
    'storages',
    'pytils',
    'googlecharts',
    'sslserver',
    'django_comments',
    'mptt',
    'tagging',
    'zinnia',
    'django_pygments',

    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.galleries",
    "mezzanine.twitter",
    "mezzanine.accounts",

    # 'apps.meetup',
    # 'apps.subscribers',
    'apps.frontend',
    'apps.tasks',

)

# if DEBUG:
#    INSTALLED_APPS += ('debug_toolbar',)

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

SERIALIZATION_MODULES = {
    'json-pretty': 'project.serializers.json_pretty',
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--failed', '--nologcapture']

import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///{0}'.format(
            os.path.join(ROOT_PATH, 'project.db'))
    )
}

# security stuff
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECRET_KEY = 'pynsk'
ZINNIA_MARKUP_LANGUAGE = 'markdown'
ZINNIA_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.admonition',
    'markdown.extensions.codehilite',
    'markdown.extensions.headerid',
    'markdown.extensions.meta',
    'markdown.extensions.nl2br',
    'markdown.extensions.sane_lists',
    'markdown.extensions.smarty',
    'markdown.extensions.toc',
    'markdown.extensions.wikilinks'
]

USE_MODELTRANSLATION = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
FILE_UPLOAD_PERMISSIONS = 0o644
# Full filesystem path to the project.
PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

BOWER_INSTALLED_APPS = (
    'jquery#2',
    'bootstrap#3.3.6',
    'bootstrap-material-design',
    'underscore',
)

if DJANGO_VERSION < (1, 9):
    del TEMPLATES[0]["OPTIONS"]["builtins"]

CACHES = {
    'default': {
        # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': '127.0.0.1:11211',
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATES[0]['OPTIONS']['context_processors']

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
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

SITE_PREFIX = 'blog/'
BLOG_SLUG = '/blog/'
# PAGES_SLUG = '/pages/'
# APPEND_SLASH = True


# THEME

JQUERY_FILENAME = 'jquery.js'

#####################
# PAGEDOWN SETTINGS #
#####################
RICHTEXT_WIDGET_CLASS = 'mezzanine_pagedown.widgets.PageDownWidget'
RICHTEXT_FILTER = 'mezzanine_pagedown.filters.custom'
RICHTEXT_FILTERS = (RICHTEXT_FILTER,)
PAGEDOWN_MARKDOWN_EXTENSIONS = ('extra', 'codehilite', 'toc')
RICHTEXT_FILTER_LEVEL = 3
PAGEDOWN_SERVER_SIDE_PREVIEW = True

try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())

try:
    from .local_settings import *
except ImportError as e:
    print(e)

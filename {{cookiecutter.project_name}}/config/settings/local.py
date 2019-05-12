from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://0.0.0.0:8080',
)

INSTALLED_APPS += [
    'corsheaders'
]

# 3rd party middleware
# This middleware need to be before CommonMiddleware
common_index = MIDDLEWARE.index('django.middleware.common.CommonMiddleware')
MIDDLEWARE.insert(common_index, 'corsheaders.middleware.CorsMiddleware')

FRONTEND_DIST_DIR = os.path.join(BASE_DIR, 'frontend', 'dist')
TEMPLATES[0]['DIRS'].append(FRONTEND_DIST_DIR)
STATICFILES_DIRS.append(os.path.join(FRONTEND_DIST_DIR, 'static'))

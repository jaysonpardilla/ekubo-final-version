from pathlib import Path
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Security: read sensitive values from environment in production
# IMPORTANT: set `SECRET_KEY` in your Render/GitHub Actions env for production.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-d!328^d((@e2_61s13s3q9=1w!g#^u5s9sk4wyjs_418#-05=t')

# Toggle DEBUG via env var. Default to False for safety when pushing to GitHub.
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS can be provided as a comma-separated string in env
# Default to '*' (allow all) for now per request; override in production env.
_allowed = os.environ.get('ALLOWED_HOSTS', '*')
ALLOWED_HOSTS = [h for h in _allowed.split(',') if h] or ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
    'chat',
    'products', 
    'manage_business',                
    'shops', 
    'captcha'
]

# Optional Cloudinary apps: only enable when env vars are set
if os.environ.get('CLOUDINARY_URL') or os.environ.get('CLOUDINARY_CLOUD_NAME'):
    INSTALLED_APPS += [
        'cloudinary',
        'cloudinary_storage',
    ]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'chat.middleware.UpdateLastSeenMiddleware',

]


USE_L10N = True

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'chat.context_processors.store_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

# Channel layer: use Redis in production via REDIS_URL env var
REDIS_URL = os.environ.get('REDIS_URL', os.environ.get('CHANNEL_REDIS_URL', 'redis://127.0.0.1:6379'))
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_URL],
        },
    },
}


DATABASES = {
    # Use SQLite by default for local development and when no DATABASE_URL is provided.
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# If a DATABASE_URL env var is provided (e.g., Render Postgres), use it instead
if os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.parse(os.environ['DATABASE_URL'], conn_max_age=600)


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

EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Use Cloudinary for media when CLOUDINARY_URL is set
if os.environ.get('CLOUDINARY_URL') or os.environ.get('CLOUDINARY_CLOUD_NAME'):
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
    # Optional: configure CLOUDINARY_STORAGE dict if detailed creds provided
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
        'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
        'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
    }

# Use WhiteNoise compressed manifest storage for static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Production security settings: enabled when DEBUG is False
if not DEBUG:
    # Redirect HTTP to HTTPS
    SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'True') == 'True'
    # Cookies
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    # HSTS
    SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', 31536000))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get('SECURE_HSTS_INCLUDE_SUBDOMAINS', 'True') == 'True'
    SECURE_HSTS_PRELOAD = os.environ.get('SECURE_HSTS_PRELOAD', 'True') == 'True'
    # Referrer policy
    SECURE_REFERRER_POLICY = os.environ.get('SECURE_REFERRER_POLICY', 'no-referrer-when-downgrade')
    # Other secure defaults
    X_FRAME_OPTIONS = 'DENY'

# settings.py
AUTH_USER_MODEL = 'chat.CustomUser'

AUTHENTICATION_BACKENDS = (
    'chat.auth_backends.EmailBackend',  # Make sure to point to your custom backend
    'django.contrib.auth.backends.ModelBackend',  # Default backend for fallback
)

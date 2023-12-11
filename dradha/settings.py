"""
Django settings for dradha project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os 
# % pip install django-environ
import environ
environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    ## LOCAL
    # dradha apps
    'useraccounts.apps.UseraccountsConfig',
    ## THIRD PARTY
    # django-cors-headers
    'corsheaders',
    # django-rest-framework
    'rest_framework',
    # rest-framework-simplejwt
    'rest_framework_simplejwt',
    # django-rest-framework and required for dj-rest-auth
    'rest_framework.authtoken',
    # django-allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # django-allauth providers
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.instagram',
    # dj-rest-auth
    'dj_rest_auth',
    'dj_rest_auth.registration',
    ## DJANGO 
    # django boilerplate and required for django-allauth
    'django.contrib.auth',
    'django.contrib.messages',
    # django boilerplate
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    # django-cors-headers
    'corsheaders.middleware.CorsMiddleware',
    # django boilerplate
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django-allauth
    "allauth.account.middleware.AccountMiddleware",
]

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    'USER_ID_FIELD': 'userId',
    'USER_ID_CLAIM': 'user_id',
    'SIGNING_KEY': JWT_SECRET_KEY,
}

# django rest framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        #'dj_rest_auth.utils.JWTCookieAuthentication',
    ),
}

CORS_ALLOWED_ORIGINS = [
    "https://dradha.co",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

ROOT_URLCONF = 'dradha.urls'

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
                # via django-allauth
                'django.template.context_processors.request',
            ],
        },
    },
]

# django-allauth provider-specific settings
SOCIALACCOUNT_PROVIDERS = {
    'github': {
        
    },
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    }
}

SOCIALACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_REQUIRED = False

# https://dj-rest-auth.readthedocs.io/en/latest/installation.html#registration-optional
# dj-rest-auth: for enabling standard registration. 
SITE_ID = 1             # enabling standard registration. 
REST_USE_JWT = True     # use JSON web tokens

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'dradha.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dradhaserver'
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL='useraccounts.User'

REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'useraccounts.serializers.UserSerializer'
}

# login 
LOGIN_URL='/admin/login/'

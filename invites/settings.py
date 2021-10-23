"""
Django settings for django_invite_project project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

try:

    from .local_settings import *

except ImportError:

    raise Exception("A local settings.py file is required to run this project")

'''
You should define LOCAL_SECRET_KEY , LOCAL_DEBUG , DATABASE_ENGINE , DATABASE_NAME , DATABASE_USER,
DATABASE_PASSWORD , DATABASE_HOST , DATABASE_PORT in local_settings.py. It is git ignored.

'''

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = LOCAL_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = LOCAL_DEBUG 

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    
    'rest_framework',
    'user_invite',
    'accounts',
    'corsheaders',
    'tinymce',
    'log',
    'django_celery_results',
    'django_celery_beat',
    'django_elasticsearch_dsl',
    'django_keycloak',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django_keycloak.middleware.BaseKeycloakMiddleware',
    #'django_keycloak.middleware.BaseKeycloakMiddleware',
    #'django_keycloak.middleware.RemoteUserAuthenticationMiddleware',
]

ROOT_URLCONF = 'invites.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'invites.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE' : DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'USER' : DATABASE_USER,
        'PASSWORD' : DATABASE_PASSWORD,
        'PORT' : DATABASE_PORT,
        'HOST' : DATABASE_HOST
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'django_keycloak.auth.backends.KeycloakAuthorizationCodeBackend',
]

#keycloak settings
#LOGIN_URL = 'keycloak_login'
#KEYCLOAK_OIDC_PROFILE_MODEL = 'django_keycloak.RemoteUserOpenIdConnectProfile'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR , 'invites/static')
]


MEDIA_ROOT = os.path.join(BASE_DIR , 'files')
MEDIA_URL = '/files/'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dramatic225@gmail.com'
EMAIL_HOST_PASSWORD = 'mohsen1160417237'
EMAIL_PORT = 25
EMAIL_USE_TLS = True

REST_FRAMEWORK = {

    'DEFAULT_AUTHENTICATION_CLASSES' : (

        'rest_framework_simplejwt.authentication.JWTAuthentication' ,
    ) ,
}

AUTH_USER_MODEL = 'accounts.User'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

#CELERY STUFF

CELERY_BROKER_URL = LOCAL_CELERY_BROKER_URL
CELERY_RESULT_BACKEND = LOCAL_CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

from celery.schedules import crontab


#elastic search settings

ELASTICSEARCH_DSL={
    'default': {
        'hosts': 'localhost:8000'
    },
}
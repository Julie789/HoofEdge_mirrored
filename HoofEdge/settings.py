"""
Django settings for HoofEdge project.

Generated by 'django-admin startproject' using Django 2.0b1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
#import django_heroku
import dj_database_url
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w#c2p$9qpf@+%_f14c9g1%4lm*o0s2ht^*+4mx^77l($)l!1!6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'mathfilters',
    'django.contrib.humanize',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
    'star_ratings',
    'social_django',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'HoofEdge.urls'

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
                'cart.context_processors.cart',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',

            ],
        },
    },
]

WSGI_APPLICATION = 'HoofEdge.wsgi.application'
# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
       'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd6bbf4t3bhdkdd',
        'USER': 'kchmoffqovobgk',
        'PASSWORD': 'f29cb4481215aea87d8c89bdad182a967c7b87735ce0546fccf50d7b7b50f884',
        'HOST': 'ec2-174-129-226-234.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

#DEBUG = True



# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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

##authentication backends

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
CART_SESSION_ID = 'cart'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
#STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
DATABASES['default'] = dj_database_url.config()

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_HOST_USER = 'postmaster@sandboxbc6ddeaf638c44eb915500e924de4a02.mailgun.org'
EMAIL_HOST_PASSWORD = '5a9edaff00bfe896fc3f9a5ea720c89c-c50f4a19-fe83f5b2'
#EMAIL_PORT = 2525
EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#DEFAULT_FROM_EMAIL = 'divyakorrapati90@gmail.com'

try:
    from .local_settings import *
except ImportError:
    print('Import Error')

# Braintree settings
BRAINTREE_MERCHANT_ID = 'm2f4z4nc66t2sjcx'
BRAINTREE_PUBLIC_KEY = '7kb3cs9tskxvw9y3'
BRAINTREE_PRIVATE_KEY = '1611f4052d262ac8231a9b4d205f1733'

from braintree import Configuration, Environment

Configuration.configure(
    Environment.Sandbox,
    # Environment.Production,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

import os
import sys
from twilio.rest import Client

TWILIO_ACCOUNT_SID = 'ACd5f5b31ba23cc6ea6b440fef9484747b'
TWILIO_AUTH_TOKEN = '95e661f7b2303fe50f0f08c6d4bc3ea1'

#account_sid = os.getenv['TWILIO_ACCOUNT_SID']
#auth_token = os.environ[TWILIO_AUTH_TOKEN]
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379
#REDIS_DB = 1

##SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'AIzaSyCbtMRLsxyHsjAgk7kwD2pgQ6jT8cktxV8'
SOCIAL_AUTH_FACEBOOK_KEY = '344132709804760' ##APP ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'b978a64c0fa8e7762bffdfdc8e922641' ##APP Secret



import os
from pathlib import Path

import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

STRIPE_PUB_KEY = 'pk_test_51MrvLrASHqKrpvFNBehFmvXQy700RBsqxDBf2oYOnq691hBOYQY3dTzpIk5J1DmYjzeCohtGyxCfBnbpkbopOWX9004sE7Rg8G'
STRIPE_SECRET_KEY = 'sk_test_51MrvLrASHqKrpvFNnuQYTuiOqYS0ZXVvvQOeSJLKVGe6UDskUgub8e02HhieLLrx2ZcWlh7BKcLHgiAcIQo6ksNF00NbEQVN7E'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ['store-uz.onrender.com', '127.0.0.1:8000']

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


WEBSITE_URL = RENDER_EXTERNAL_HOSTNAME


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    "crispy_forms",
    "crispy_bootstrap5",
    'store',
    'users',
    'products',
    'sorl.thumbnail',
]

CSRF_TRUSTED_ORIGINS = [
    'https://store-uz.onrender.com',
    'http://store-uz.onrender.com',
    'http://127:0.0.1:8000',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.views.for_all_pages',
                'store.views.page_name',
                'store.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'railway',
#         'USER': 'postgres',
#         'PASSWORD': 'qocYArmyXq8h0vcSgTm8',
#         'HOST': 'containers-us-west-199.railway.app',
#         'PORT': '6536',
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='postgres://abdulaziz:FsMKrHns3OVAZO37mQJQRfo7FDQsy1Wr@dpg-cjecqsrbq8nc73d2chtg-a/dbblog_qezn',
        conn_max_age=600
    )
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CART_SESSION_ID = 'cart'
SESSION_COOKIE_AGE = 86400

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'store:accounts'
LOGOUT_REDIRECT_URL = 'store:accounts'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'abdulazizkomilov2001@gmail.com'
# EMAIL_HOST_PASSWORD = '6066066aA'

# # Allauth settings
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
# ACCOUNT_EMAIL_SUBJECT_PREFIX = '[My Site] '
# ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'http'

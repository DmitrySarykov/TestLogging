"""
Django settings for testlogging project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+-90s4p7)!x!llhiw@424(6_o=r(s2@^82r@4pb2s(olm*o7bo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'testlogging.urls'

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

WSGI_APPLICATION = 'testlogging.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        # 1
        'fdebug': {
            'format': '{asctime} {levelname} {message}',
            'style': '{',
        },
        'fwarning': {
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },
        # 1 3
        'ferror': {
            'format': '{levelname} {asctime} {message} {pathname} {exc_info}',
            'style': '{',
        },
        #  5
        'ferror_mail': {
            'format': '{levelname} {asctime} {message} {pathname}',
            'style': '{',
        },
        # 2 
        'finfo': {
            'format': '{asctime} {levelname} {module} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },    
    'handlers': {
        # 1
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'fdebug',
            'filters': ['require_debug_true'],
        },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'fwarning',
            'filters': ['require_debug_true'],
        },
        'errorcrit': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'ferror',
            'filters': ['require_debug_true'],
        },
        # 2 
        'general': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'finfo',
            'filename': 'general.log',
            'filters': ['require_debug_false'],
        },
        # 3
        'errors': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'ferror',
            'filename': 'errors.log',
        },
        # 4
        'security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'finfo',
            'filename': 'security.log',
        },
        # 5
        'mail': {
            'level': 'ERROR',
            'formatter': 'ferror_mail',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
        }        
    },
    'loggers': {
        'django': {
            'handlers': ['debug','warning','errorcrit','general'],
            'level': 'DEBUG',
            'propagate': True,
        },
        #  3
        'django.request': {
            'handlers': ['errors','mail'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['errors','mail'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.template': {
            'handlers': ['errors'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db_backends': {
            'handlers': ['errors'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 4
        'django.security': {
            'handlers': ['security'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
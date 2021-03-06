﻿"""
Django settings for recruitment project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1ra_x&w^q0erfsnd&3r&p_e-ygaptns8zj^a=r8-bj-cop@*yt'

# SECURITY WARNING: don't run with debug turned on in production!   sdas s

ALLOWED_HOSTS = []


# Application definition
#     'grappelli',  #放在最前面
#     'debug_toolbar',

INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'interview.apps.CandidateConfig',
    'dingtalkchatbot',
    'registration',
    'rest_framework',
    'django_celery_beat',
    'running',

]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

ACCOUNT_ACTIVATION_DAYS = 7
INCLUDE_REGISTER_URL = "/accounts/register/"
SIMPLE_BACKEND_REDIRECT_URL = "/accounts/login/"

MIDDLEWARE = [
 	'django.middleware.cache.UpdateCacheMiddleware',
    # 'interview.performance.PerformanceAndExceptionLoggerMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',   
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/2.2.4/jquery.min.js',
}

ROOT_URLCONF = 'recruitment.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'recruitment.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_mysql',
        'USER': 'root',
        'PASSWORD': 'P@ssword',
        'HOST': '127.0.0.1',
	    'PORT': 3307,
    },
    'slave': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_mysql',
        'USER': 'root',
        'PASSWORD': 'P@ssword',
        'HOST': '127.0.0.1',
	    'PORT': 3308,
    }
}

#这里配置读写库
# DATABASE_ROUTERS = ['settings.router.DatabaseRouter']

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "TIMEOUT":300,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

CACHE_MIDDLEWARE_SECONDS = 600
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# session 设置
# SESSION_COOKIE_NAME = "sessionid"       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH = "/"               # Session的cookie保存的路径（默认）
# SESSION_COOKIE_DOMAIN = None             # Session的cookie保存的域名（默认）
# SESSION_COOKIE_SECURE = False            # 是否Https传输cookie（默认）
# SESSION_COOKIE_HTTPONLY = True           # 是否Session的cookie只支持http传输（默认）
# SESSION_COOKIE_AGE = 3600 * 24           # Session的cookie失效日期（2周）（数字为秒数）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # 是否关闭浏览器使得Session过期（默认）
# SESSION_SAVE_EVERY_REQUEST = True       # 是否每次请求都保存Session，默认修改之后才保存（默认）
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

#日志

LOGGING = {
    "version" : 1,
    "disable_existing_loggers" :False,
    "formatters":{  #日志格式
        "simple":{
            'format':'%(asctime)s %(name)-12s %(lineno)d'
        },
        'standard': {
            'format': '[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] '
                      '[%(levelname)s]- %(message)s'},
    },
    "filters":{},   #过滤
    "handlers" :{   #定义具体处理日志的方式
        "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter":"simple",
        },
        "file":{
            "level":"INFO",
            "class":"logging.FileHandler",
            "formatter":"simple",
            "filename":os.path.join(os.path.dirname(BASE_DIR), 'recruitment.admin.log')
        },
        "performance":{
            "level":"INFO",
            "class":"logging.FileHandler",
            "formatter":"standard",
            "filename":os.path.join(os.path.dirname(BASE_DIR), 'recruitment.performance.log')
        },
        "signal_processor":{
            "level":"INFO",
            "class":"logging.FileHandler",
            "formatter":"standard",
            "filename":os.path.join(os.path.dirname(BASE_DIR), 'recruitment.signal_processor.log')
        },
    },
    # "root":{
    #     "handlers":["console", "file"],
    #     "level":"INFO",
    # },
    "loggers":{  #配置用哪几种handlers来处理日志
        # 类型 为 django 处理所有类型的日志， 默认调用
        # 'django': {
        #     'handlers': ['file', 'console'],
        #     'level': 'INFO',
        #     'propagate': False
        # },
        # # log 调用时需要当作参数传入
        # 'log': {
        #     'handlers': [ 'console', 'file'],
        #     'level': 'INFO',
        #     'propagate': True
        # },
        'interview.performance': {
            'handlers': [ 'performance'],
            'level': 'INFO',
            'propagate': False
        },
        'settings.router': {
            'handlers': [ 'performance'],
            'level': 'INFO',
            'propagate': False
        },
        'interview.signal_processor': {
            'handlers': [ 'signal_processor'],
            'level': 'INFO',
            'propagate': False
        }
    },
}




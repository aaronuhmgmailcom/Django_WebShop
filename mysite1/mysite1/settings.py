"""
Django settings for mysite1 project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qv=42t43*oik5kd(u$zuii$z-5pz*t$^n=2+!iby-$2b8v!#+r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'users',
    'orders',
    'download',
    'uploads',
    'user_comment',
    'order',
    'order_item',
    'price_history',
    'product',
    'product_class',
    'rotation',
    'search_history',
    'shopping_cart',
    'user_wallet',
    'UserAddress',
    'btoken',
    'topic',
    'message',
    'payment',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middleware.mymiddleware.VisitLimit',
    'middleware.mymiddleware.MyMiddleWare',
]

ROOT_URLCONF = 'mysite1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':  [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'mysite1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'WebShopDB',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '176.215.66.101',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True
#True表示在数据库中写入的是标准时间，在DJANGO中的模版夜中根据配置的市区时间，自动计算当市区时间
#FALSE 在数据库中直接写入的就是当前市区的时间
#钱后端分离后，不再使用DJANGO模版了，选择FALSE
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
#         'LOCATION': 'my_cache_table',
#         'TIMEOUT': 300,  # 缓存保存时间 单位秒，默认值为300,
#         'OPTIONS': {
#             'MAX_ENTRIES': 300,  # 缓存最大数据条数
#             'CULL_FREQUENCY': 2,  # 缓存条数达到最大值时 删除1/x的缓存数据
#         }
#     }
# }
SESSION_COOKIE_AGE = 60 * 60
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # 固定写法
# EMAIL_HOST = 'smtp.qq.com' # 腾讯QQ邮箱 SMTP 服务器地址
# EMAIL_PORT = 25  # SMTP服务的端口号
# EMAIL_HOST_USER = '**@qq.com'  # 发送邮件的QQ邮箱
# EMAIL_HOST_PASSWORD = 'qyijsjqyobdrvbhgdwe'  # 在QQ邮箱->设置->帐户->“POP3/IMAP......服务” 里得到的在第三方登录QQ邮箱授权码
# EMAIL_USE_TLS = True  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)默认false

STATIC_ROOT = '/home/tarena/PycharmProjects/Django_WebShop/mysite1_static'
ADMINS = [('peter', '**@qq.com')]
SERVER_EMAIL = '**@qq.com'

# CACHES = {
#     "default": {
#             "BACKEND": "django_redis.cache.RedisCache",
#             "LOCATION": "redis://127.0.0.1:6379",
#             "OPTIONS": {
#                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             }
#         }
# }

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)

JWT_TOKEN_KEY='123456'

SMS_ACCOUNT_ID = '8a216da87380115d017389546bb802f5'
SMS_ACCOUNT_TOKEN = '12444d5592d247b2af0e5cc10bf666a0'
SMS_APP_ID = '8a216da87380115d017389546c9e02fb'
SMS_TEMPLATE_ID = '1'

ALIPAY_APPID='2021000116664332'
ALIPAY_KEY_DIR= os.path.join(BASE_DIR,'static/key_file/')
ALIPAY_RETURN_URL='http://127.0.0.1:8000/payment/result/'
ALIPAY_NOTIFY_URL='http://127.0.0.1:8000/payment/result/'
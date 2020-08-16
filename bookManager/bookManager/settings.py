"""
Django settings for bookManager project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

"""
__file__：在pycharm中，返回当前文件的绝对路径。在cmd中，返回文件名。
os.path.abspath(path)：返回path的绝对路径。
os.path.dirname(path):返回path所在目录。
# BASE_DIR 指向当前工程的根目录
"""
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 项目启动会加载setting.py文件，会打印这个全局变量。
print("settings.py--->", BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3sw25)^22%!e@2!0amo^h0)ip747y#-&r6jucv4&*#1v^%yo$^'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式，会显示详细的错误信息；修改代码后，会自动重启服务。
DEBUG = True
# 设置DEBUG为False，则必须设置allowed_hosts。表示服务器的访问IP
# 可以设置为域名，那客户端访问的时候，只能通过域名访问。
# 可以设置为具体的IP，那客户端访问的时候，只能通过IP访问。
# 可以设置为*，表示域名和IP都可以访问。(不推荐这么用)
ALLOWED_HOSTS = ['*']
# 设置DEBUG为True，则不需要设置allowed_hosts。
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 注册book应用（方式1）
    # 'book',
    # 注册book应用（方式2）
    'book.apps.BookConfig',
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

ROOT_URLCONF = 'bookManager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 配置模板查找路径
        'DIRS': [
            os.path.join(BASE_DIR, "templates")
        ],
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

WSGI_APPLICATION = 'bookManager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': "127.0.0.1",  # localhost也可以
            'PORT': 3306,
            'USER': "root",
            'PASSWORD': "mysql",
            'NAME': "py2888",
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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# 语言设置
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

# 时区设置
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# 访问静态文件的url前缀
STATIC_URL = '/static/'
# 静态文件的存放路径，查找静态文件就从该配置的项中进行依次查找，直到找到为止。
STATICFILES_DIRS = [
    # 配置项目的静文文件存放目录
    os.path.join(BASE_DIR, "static"),
    # 配置应用的静态文件存放目录
    os.path.join(BASE_DIR, "book/static"),
]

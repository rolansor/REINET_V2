"""
Django settings for REINET project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u$($fb52#aah83vn8dg_kt@77#yar3jewb29@2&qt4**u@mpv='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'swampdragon',
	'swampdragon_auth',
	'cities_light',
	'ipware',
	'usuarios',
	'ofertas_demandas',
<<<<<<< HEAD
	'incubacion',
=======
    'incubacion'
>>>>>>> 31cf350c0d42cc4aeb27c5410896184729def6e5
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.middleware.security.SecurityMiddleware',
)

REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': (
		'rest_framework.permissions.IsAuthenticated',
	),
	'DEFAULT_AUTHENTICATION_CLASSES': (
		'rest_framework.authentication.SessionAuthentication',
		'rest_framework.authentication.BasicAuthentication',
	),
}

ROOT_URLCONF = 'REINET.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': ['template/'],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.template.context_processors.debug',
				'django.template.context_processors.request',
				'django.contrib.auth.context_processors.auth',
				'django.contrib.messages.context_processors.messages',
				'django.core.context_processors.request',
			],
		},
	},
]


WSGI_APPLICATION = 'REINET.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
	  'default': {
		  'ENGINE': 'django.db.backends.mysql',
		  'NAME': 'Reinet',
		  'HOST': '201.183.227.87',
		  'PORT':'13306',
		  'USER':'reinet',
		  'PASSWORD':'ReInEt2015'
	  }
}


#esto para probar localmente mientras el servidor murio
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'Reinet',
#        'HOST': '192.168.1.39',
#        'PORT':'3306',
#        'USER':'reinet',
#        'PASSWORD':'ReInEt2015'
#    }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'es-ec'

TIME_ZONE = 'America/Guayaquil'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SOUTH_MIGRATION_MODULES = {
	'cities_light': 'cities_light.south_migrations',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
	os.path.join(BASE_DIR,  'template'),
)

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)


MEDIA_ROOT = (
	os.path.join(BASE_DIR, 'media')
)

MEDIA_URL = '/media/'

LOGIN_URL = '/iniciarSesion/'

CSRF_FAILURE_VIEW = 'usuarios.views.csrf_failure'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#Aqui va la configuracion del servidor de correo (GMAIL)
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'reinetespol@gmail.com' # cuenta reinet en gmail
EMAIL_HOST_PASSWORD = 'reinet1234' # clave de cuenta reinet
EMAIL_USE_TLS = True

#configuracion de swampdragon para real time
#SWAMP_DRAGON_CONNECTION = ('swampdragon.connections.sockjs_connection.DjangoSubscriberConnection', '/data')
#SWAMP_DRAGON_CONNECTION = ('REINET.mysql_connection.MysqlHeartbeatConnection', '/data')
SWAMP_DRAGON_CONNECTION = ('swampdragon_auth.socketconnection.HttpDataConnection', '/data')
DRAGON_URL = 'http://127.0.0.1:9999/'

#Si realizan cambios en este archivo, que sean los technical leaders los que lo realicen.
#Si algun programador necesita hacer algun cambio conversar con su technical.
#Comentar que cambio,cuando se lo hizo y por que se lo realizo.

#para ejecutar test en servidor sqlite
#if 'test' in sys.argv:
#    DATABASES['default']={
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'reinet_test.db'),
#   }

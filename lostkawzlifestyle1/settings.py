"""
Django settings for lostkawzlifestyle1 project.

Generated by 'django-admin startproject' using Django 1.9.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

from decouple import config, Csv
import dj_database_url
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'sekizai',
    'djangocms_admin_style',
    'filer',
    'easy_thumbnails',
    'mptt',
    'reversion',                
    'cms',
    'menus',
    'treebeard',
   
    'storages',
    'django.contrib.sites',
    'djangocms_text_ckeditor',
    'djangocms_link',
    'djangocms_file',
    'djangocms_picture',
    'djangocms_video',
    'djangocms_googlemap',
    'djangocms_snippet',
    'djangocms_style',
    'djangocms_column',
    'djangocms_youtube',
    'absolute',
    'aldryn_forms',
    'aldryn_forms.contrib.email_notifications',
    'captcha',
    'emailit',
    'aldryn_apphooks_config',
    'aldryn_mailchimp',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_background_image',
    'lostkawzlifestyle1',
    
    
    'aldryn_people',
    'aldryn_reversion',
    'aldryn_translation_tools',
    'aldryn_gallery',
    'aldryn_boilerplates',
    
    
    'parler',
    'sortedm2m',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]



THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)

ROOT_URLCONF = 'lostkawzlifestyle1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'cms.context_processors.cms_settings',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'lostkawzlifestyle1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

CMS_TEMPLATES = [
    ('base.html', 'base'),
    ('content.html', 'content page template'),
     ('gallery.html', 'gallery page template'),
    
]



# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
   
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True 

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
AWS_STORAGE_BUCKET_NAME = config('BUCKET_NAME')
AWS_CLOUDFRONT_DOMAIN = config('CD_DOMAIN')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID') 
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME   
AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }

MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'



    


STATIC_ROOT = 'lostkawzlifestyle1/staticfiles/'

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'custom_storages.StaticStorage'

STATIC_URL = "https://%s/%s/" % (AWS_CLOUDFRONT_DOMAIN, STATICFILES_LOCATION)









STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

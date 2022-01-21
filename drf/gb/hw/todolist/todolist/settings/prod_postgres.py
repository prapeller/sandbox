from todolist.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres_user',
        'NAME': 'todolist_db',
        'PASSWORD': 'superpassword',
        'HOST': 'db',
        'PORT': '5432'
    }
}
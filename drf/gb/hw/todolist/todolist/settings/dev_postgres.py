from todolist.settings.dev import *

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += [
    'django_extensions',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'postgres_user',
        'NAME': 'todolist_db',
        'PASSWORD': 'superpassword',
        'HOST': '127.0.0.1',
        'PORT': '54325'
    }
}
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'your_db_name'),
        'USER': os.getenv('POSTGRES_USER', 'your_db_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'your_db_password'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}
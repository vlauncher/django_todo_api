from .base import *
import dj_database_url

# Postgres Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases



DATABASES = {
    'default': dj_database_url.config(
        default= environ.get('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

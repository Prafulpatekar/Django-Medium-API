from .base import * #noqa
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY",default="71q7FAUtdTV94A8oRCCrTFoDBmRG2tdCZadnnobbarvh6Tid9hI")

DEBUG = True

# ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="mailhog")
EMAIL_PORT = env("EMAIL_PORT")
DEFAULT_FROM_EMAIL = "support@djangomedium.site"
DOMAIN = env("DOMAIN")
SITE_NAME = "Django Medium APP"
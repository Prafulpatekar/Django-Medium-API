from .base import * #noqa
from .base import env

SECRET_KEY = env("DJANGO_SECRET_KEY",default="71q7FAUtdTV94A8oRCCrTFoDBmRG2tdCZadnnobbarvh6Tid9hI")

DEBUG = True

# ALLOWED_HOSTS = []

CSRF_TRUSTED_ORIGINS = ["http://localhost:8090"]
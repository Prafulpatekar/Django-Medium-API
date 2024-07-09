from django.apps import AppConfig
from django.utils.translation import gettext_lazy

class RatingsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.ratings"
    verbose_name = gettext_lazy("Rating")
    verbose_name_plural = gettext_lazy("Ratings")
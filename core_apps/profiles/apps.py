from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class ProfilesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.profiles"
    verbose_name = gettext_lazy("Profile")
    verbose_name_plural = gettext_lazy("Profiles")

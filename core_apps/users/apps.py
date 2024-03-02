from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.users"
    verbose_name = gettext_lazy("User")
    verbose_name_plural = gettext_lazy("Users")

from django.apps import AppConfig
from django.utils.translation import gettext_lazy

class CommonConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.common"
    verbose_name = gettext_lazy("Common")
    verbose_name_plural = gettext_lazy("Commons")
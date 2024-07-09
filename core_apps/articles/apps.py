from django.apps import AppConfig
from django.utils.translation import gettext_lazy

class ArticlesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.articles"
    verbose_name = gettext_lazy("Article")
    verbose_name_plural = gettext_lazy("Articles")
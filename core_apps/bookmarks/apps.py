from django.apps import AppConfig
from django.utils.translation import gettext_lazy

class BookmarksConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core_apps.bookmarks"
    verbose_name = gettext_lazy("Bookmark")
    verbose_name_plural = gettext_lazy("Bookmarks")

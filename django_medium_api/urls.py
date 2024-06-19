from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Django Medium API",
        default_version="v1",
        description="API endpoints for Django Medium API Course",
        contact=openapi.Contact(email="prafulpatekar.dev@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True, # make false to protect the documentation
    permission_classes=(permissions.AllowAny,), # add appropriate permission
)


urlpatterns = [

    path("redoc/",schema_view.with_ui("redoc",cache_timeout=0)), # third party package to get UI for API docs
    path(settings.ADMIN_URL, admin.site.urls),

]

admin.site.site_header = "Django Medium API Admin" # Text will display at admin site

admin.site.site_title = "Django Medium API Admin Portal" # displayed on browser tab

admin.site.index_title = "Welcome to Django Medium API Portal" # display at admin index page

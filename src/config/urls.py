from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings

from drf_yasg.generators import OpenAPISchemaGenerator

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', include("schema.urls")),
]



from django.urls import path

from .views import SchemaView


urlpatterns = [
  
  # schema view
  path("view/", SchemaView.as_view(), name="view"),
  
]
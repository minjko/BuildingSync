from django.urls import path

from django.contrib.auth import views as auth_views


app_name = "user"
urlpatterns = [
  # login
  path("login/", auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),

]
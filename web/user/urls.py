from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from .views  import google_login, google_callback

urlpatterns = [
    path("google/login/", google_login, name="google_login"),
    path("google/callback/", google_callback, name="google_callback"),
]
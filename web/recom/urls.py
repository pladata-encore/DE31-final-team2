from django.urls import path, include
from . import views

urlpatterns = [
    path('wineasy/', views.recom, name='recom'),
]
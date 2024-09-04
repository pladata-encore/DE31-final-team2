from django.urls import path, include
from . import views

urlpatterns = [
    path('wine_recommend/', views.recom, name='recom'),
]
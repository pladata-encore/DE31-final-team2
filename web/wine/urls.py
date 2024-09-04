from django.urls import path
from django.views.generic import TemplateView
from .views import WineListView, WineDetailView

urlpatterns = [
    path('', TemplateView.as_view(template_name="wine_list.html"), name='wine-list'),
    path('<int:pk>/', TemplateView.as_view(template_name="wine_detail.html"), name='wine-detail'),
    path('api/wines/', WineListView.as_view(), name='wine-list-api'),
    path('api/wines/<int:pk>/', WineDetailView.as_view(), name='wine-detail-api'),
]
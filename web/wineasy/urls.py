from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('recom/', include('review.urls')),
    #path('wine/', include('wine.urls')),
    path('main/', include('main.urls')),
    path('account/', include('user.urls')),
    path('account/', include('allauth.urls')),
    
    # 아래는 변수현
    path('', include('recom.urls')),
]
#from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Wine
from .serializers import WineSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


# pagenation 많은 결과
class LargeResultsSetPagination(PageNumberPagination):
    page_size : 100
    page_query_param = 'page_size'
    max_page_size= 10000
    
# pagenation 적은 결과    
class StandardResultsSetPaginaion(PageNumberPagination):
    page_size = 20 
    page_query_param = 'page_size'
    max_page_size = 100000   

# 전체 조회  
class WineListView(generics.ListAPIView):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
    pagination_class = StandardResultsSetPaginaion

    # 필터링, 정렬 기능 추가
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, OrderingFilter]
    search_fields = ['vintage_name'] # 검색 가능한 필드
    filterset_fields = ['type_id', 'country', 'volume']  # 필터링 가능한 필드
    ordering_fields = ['ratings_average', 'price_usd']  # 정렬 가능한 필드        
    
    
#상세 조회
class WineDetailView(APIView):
    def get(self, request, pk):
        wine = get_object_or_404(Wine, pk=pk)      
        serializer = WineSerializer(wine)        
        return Response(serializer.data)
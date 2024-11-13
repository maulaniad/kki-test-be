from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from api.category.serializers import CategorySerializer
from database.models import Category
from helpers.pagination import StandardPagination


class CategoryListView(ListCreateAPIView):
    pagination_class = StandardPagination
    serializer_class = CategorySerializer
    queryset = Category.objects.all().order_by('-created_at')
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'created_at']


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "id"

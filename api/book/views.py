from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from api.book.serializers import BookSerializer
from database.models import Book
from helpers.pagination import StandardPagination


class BookListView(ListCreateAPIView):
    pagination_class = StandardPagination
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('-created_at')
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'author', 'created_at']


class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "id"

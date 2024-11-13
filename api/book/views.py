from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from api.book.serializers import BookSerializer
from database.models import Book
from helpers.pagination import StandardPagination


class BookListView(ListCreateAPIView):
    queryset = Book.objects.all().order_by('-created_at')
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'author', 'created_at']
    pagination_class = StandardPagination
    serializer_class = BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"

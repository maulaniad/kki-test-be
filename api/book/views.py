from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.book.serializers import BookSerializer
from database.models import Book
from helpers.pagination import StandardPagination


class BookListView(ListCreateAPIView):
    pagination_class = StandardPagination
    serializer_class = BookSerializer
    queryset = Book.objects.all().order_by('-created_at')


class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "id"

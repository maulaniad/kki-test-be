from django.urls import path

from api.book.views import BookListView, BookDetailView


app_name = "book"

urlpatterns = [
    path("", BookListView.as_view(), name="list-book"),
    path("<int:id>", BookDetailView.as_view(), name="detail-book"),
]

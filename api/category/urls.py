from django.urls import path

from api.category.views import CategoryListView, CategoryDetailView


app_name = "category"

urlpatterns = [
    path("", CategoryListView.as_view(), name="list-category"),
    path("<int:id>", CategoryDetailView.as_view(), name="detail-category"),
]

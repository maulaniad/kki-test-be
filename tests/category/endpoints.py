from django.urls import reverse


class CategoryEndpoints:
    list_category = reverse("category:list-category")
    detail_category = reverse("category:detail-category")

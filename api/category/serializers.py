from rest_framework.serializers import ALL_FIELDS, ModelSerializer

from database.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ALL_FIELDS

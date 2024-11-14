from rest_framework.serializers import ALL_FIELDS, ModelSerializer, DateTimeField

from database.models import Category


class CategorySerializer(ModelSerializer):
    created_at = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    updated_at = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    deleted_at = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Category
        fields = ALL_FIELDS

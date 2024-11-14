from rest_framework.serializers import (ALL_FIELDS,
                                        ModelSerializer,
                                        PrimaryKeyRelatedField,
                                        DateTimeField)

from api.category.serializers import CategorySerializer
from database.models import Book, Category


class BookSerializer(ModelSerializer):
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())
    created_at = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    updated_at = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)
    deleted_at = DateTimeField(format="%d-%m-%Y %H:%M:%S", read_only=True)

    class Meta:
        model = Book
        fields = ALL_FIELDS

    def to_representation(self, instance: Book):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation

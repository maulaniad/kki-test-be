from rest_framework.serializers import ALL_FIELDS, ModelSerializer, PrimaryKeyRelatedField

from api.category.serializers import CategorySerializer
from database.models import Book, Category


class BookSerializer(ModelSerializer):
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Book
        fields = ALL_FIELDS

    def to_representation(self, instance: Book):
        representation = super().to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        return representation

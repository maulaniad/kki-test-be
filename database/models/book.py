from django.db.models import CharField, FileField, ForeignKey, CASCADE

from database.models.base import BaseModel
from database.models.category import Category


class Book(BaseModel):
    title = CharField(max_length=50, db_index=True)
    author = CharField(max_length=50, null=True)
    cover = FileField(null=True)
    category = ForeignKey(Category, db_column="category_id", on_delete=CASCADE, null=True, related_name="books")

    class Meta(BaseModel.Meta):
        db_table = "book"

    def __str__(self):
        return self.title

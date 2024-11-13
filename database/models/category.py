from django.db.models import CharField

from database.models.base import BaseModel


class Category(BaseModel):
    name = CharField(max_length=255, unique=True)

    class Meta(BaseModel.Meta):
        db_table = "category"

    def __str__(self):
        return self.name

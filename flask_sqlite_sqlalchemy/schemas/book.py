from marshmallow import ma
from models.books import BookModel


class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BookModel
        load_instance = True

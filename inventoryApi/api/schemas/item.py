from ninja import ModelSchema
from api.models.item import Item


class ItemIn(ModelSchema):
    class Config:
        model = Item
        model_fields = ["name"]


class ItemOut(ModelSchema):
    class Config:
        model = Item
        model_fields = fields = ("id", "name")

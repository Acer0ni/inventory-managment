from ninja import ModelSchema
from api.models.warehouse import Warehouse


class WarehouseIn(ModelSchema):
    class Config:
        model = Warehouse
        model_fields = ["location"]


class WarehouseOut(ModelSchema):
    class Config:
        model = Warehouse
        model_fields = ["id", "location"]

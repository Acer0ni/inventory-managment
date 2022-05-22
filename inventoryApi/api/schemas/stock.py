from ninja import ModelSchema
from api.models.stock import Stock


class StockIin(ModelSchema):
    class Config:
        model = Stock
        model_fields = ["warehouse_id", "item_id", "quantity"]


class StockOut(ModelSchema):
    class Config:
        model = Stock
        model_fields = ["id", "warehouse_id", "item_id", "quantity"]

from django.db import models
from models.item import Item
from models.warehouse import Warehouse


class Stock(models.Model):
    item_id = models.ForeignKey(Item, related_name="stock", on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(
        Warehouse, related_name="stock", on_delete=models.CASCADE
    )
    quantity = models.IntegerField()

    class meta:
        UniqueConstraint = ("item_id", "warehouse_id")

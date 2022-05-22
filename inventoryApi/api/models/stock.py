from django.db import models
from .item import Item
from .warehouse import Warehouse


class Stock(models.Model):
    item_id = models.ForeignKey(Item, related_name="stock", on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(
        Warehouse, related_name="stock", on_delete=models.CASCADE
    )
    quantity = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["item_id", "warehouse_id"], name="unique location"
            )
        ]

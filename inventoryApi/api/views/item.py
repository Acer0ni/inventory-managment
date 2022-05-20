from ninja import Router, NinjaAPI
from api.models import Item
from typing import List

from api.schemas.item import ItemIn, ItemOut

api = NinjaAPI(
    title="inventory managemnet",
    description="an api for all your inventory management needs",
    version="0.0.1",
    auth=None,
    csrf=True,
)


@api.post("/", response=ItemOut)
def create_item(request, new_item: ItemIn):
    item = Item.objects.create(name=new_item.name, amount=new_item.amount)
    item.save()
    return item


@api.get("/", response=List[ItemOut])
def show_items(request):
    return Item.objects.all()

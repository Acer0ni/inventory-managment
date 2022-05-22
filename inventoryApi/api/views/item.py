from django.shortcuts import get_object_or_404
from ninja import Router
from api.models import Item
from typing import List

from api.schemas.item import ItemIn, ItemOut


router = Router(tags=["item"])


@router.post("/", response=ItemOut)
def create_item(request, new_item: ItemIn):
    item = Item.objects.create(name=new_item.name)
    item.save()
    return item


@router.get("/", response=List[ItemOut])
def show_items(request):
    return Item.objects.all()


@router.get("/{item_id}", response=ItemOut)
def get_item_by_id(request, item_id: int):
    return get_object_or_404(Item, id=item_id)


@router.put("/{item_id}", response=ItemOut)
def update_item(request, item_id: int, updated_item: ItemIn):
    item = get_object_or_404(Item, id=item_id)
    item.name = updated_item.name
    item.save()
    return item


@router.delete("/{item_id}")
def delete_item(request, item_id: int):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return "item deleted successfully"

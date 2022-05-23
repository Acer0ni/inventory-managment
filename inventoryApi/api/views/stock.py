from django.shortcuts import get_object_or_404
from ninja import Router
from api.models import Stock, Warehouse, Item
from typing import List
from ninja.errors import HttpError

from api.schemas.stock import StockIin, StockOut

router = Router(tags=["stock"])


@router.post("/", response=StockOut)
def create_stock(request, new_stock: StockIin):
    warehouse = Warehouse.objects.get(id=new_stock.warehouse_id)
    item = Item.objects.get(id=new_stock.item_id)
    stock = Stock.objects.create(
        item_id=item,
        warehouse_id=warehouse,
        quantity=new_stock.quantity,
    )
    stock.save()
    return stock


@router.get("/", response=List[StockOut])
def show_stocks(request):
    return Stock.objects.all()


@router.get("/{stock_id}", response=StockOut)
def get_stocks_by_stock_id(request, stock_id: int):
    return get_object_or_404(Stock, id=stock_id)


@router.get("/warehouse/{warehouse_id}", response=List[StockOut])
def get_stocks_by_warehouse_id(request, warehouse_id: int):
    return Stock.objects.filter(warehouse_id=warehouse_id).all()


@router.get("/warehouse/{warehouse_id}/{item_id}", response=List[StockOut])
def get_stock_in_warehouse(request, warehouse_id: int, item_id: int):
    return (
        Stock.objects.filter(warehouse_id_id=warehouse_id).filter(item_id=item_id).all()
    )


@router.put("/{stock_id}/{new_warehouse_id}/{quantity}", response=StockOut)
def move_stock(request, stock_id: int, new_warehouse_id: int, quantity: int):
    stock = get_object_or_404(Stock, id=stock_id)
    if stock.quantity < quantity:
        return HttpError(400, "not enough stock in location to move that quantity")
    new_stock = (
        Stock.objects.filter(warehouse_id_id=new_warehouse_id)
        .filter(item_id=stock.item_id)
        .first()
    )
    if not new_stock:
        warehouse = get_object_or_404(Warehouse, id=new_warehouse_id)
        item = get_object_or_404(Item, id=stock.item_id_id)
        new_stock = Stock.objects.create(
            item_id=item, warehouse_id=warehouse, quantity=0
        )
    new_stock.quantity += quantity
    stock.quantity -= quantity
    new_stock.save()
    stock.save()
    return stock


@router.put("/{stock_id}/{quantity}", response=StockOut)
def update_stock_quantity(request, stock_id: int, quantity: int):
    stock = get_object_or_404(Stock, id=stock_id)
    stock.quantity = quantity
    stock.save()
    return stock

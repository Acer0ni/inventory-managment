from django.shortcuts import get_list_or_404, get_object_or_404
from ninja import Router
from api.models import Warehouse
from typing import List

from api.schemas.warehouse import WarehouseIn, WarehouseOut

router = Router(tags=["warehouse"])


@router.post("/", response=WarehouseOut)
def create_warehouse(request, new_warehouse: WarehouseIn):
    warehouse = Warehouse.objects.create(location=new_warehouse.location)
    warehouse.save()
    return warehouse


@router.get("/", response=List[WarehouseOut])
def get_all_warehouses(request):
    return Warehouse.objects.all()


@router.get("{warehouse_id}", response=WarehouseOut)
def get_warehouse_by_id(request, warehouse_id: int):
    return get_object_or_404(Warehouse, id=warehouse_id)


@router.put("{warehouse_id}", response=WarehouseOut)
def update_warehouse(request, warehouse_id: int, updated_warehouse: WarehouseIn):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    warehouse.location = updated_warehouse.location
    warehouse.save()
    return warehouse


@router.delete("{warehouse_id}")
def delete_warehouse(request, warehouse_id: int):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    warehouse.delete()
    return "warehouse deleted successfully"

from ninja import NinjaAPI


api = NinjaAPI(
    title="inventory managemnet",
    description="an api for all your inventory management needs",
    version="0.0.1",
    auth=None,
    csrf=True,
)

from api.views.item import router as item_router
from api.views.warehouse import router as warehouse_router
from api.views.stock import router as stock_router

api.add_router("item/", item_router)
api.add_router("warehouse/", warehouse_router)
api.add_router("stock/", stock_router)

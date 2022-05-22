from ninja import NinjaAPI

api = NinjaAPI(
    title="inventory managemnet",
    description="an api for all your inventory management needs",
    version="0.0.1",
    auth=None,
    csrf=True,
)
from api.api import router as api_router

api.add_router("/", api_router)

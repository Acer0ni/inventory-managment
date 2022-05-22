from ninja import Router

router = Router()

from api.views.item import router as item_router

router.add_router("item/", item_router)

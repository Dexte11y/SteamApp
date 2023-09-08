from api.accounts import router as accounts_router
from api.inventories import router as inventories_router

all_routers = [
    accounts_router,
    inventories_router,
]

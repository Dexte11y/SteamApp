from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.inventories import InventoriesSchemaAdd
from services.inventories import InventoriesServece

router = APIRouter(
    prefix="/v1/inventories",
    tags=["Inventories"]
)


@router.get(
    "/inventories"
)
async def get_inventories(
        uow: UOWDep
):
    inventories = await InventoriesServece.get_all_inventories(uow)

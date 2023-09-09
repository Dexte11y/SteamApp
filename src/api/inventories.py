from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.inventories import InventoriesSchemaAdd
from services.inventories import InventoriesService

router = APIRouter(
    prefix="/v1",
    tags=["Inventories"]
)


@router.post(
    "/inventories"
)
async def add_inventory(
        inventory: InventoriesSchemaAdd,
        uow: UOWDep
):
    inventory_id = await InventoriesService.add_inventory(uow, inventory)
    return {"account_id": inventory_id}


@router.get(
    "/accounts/{id}/inventory"
)
async def get_inventories_by_id(
        inventory_id: int,
        uow: UOWDep
):
    inventory_by_id = await InventoriesService.get_inventories_by_id(uow, inventory_id)
    return inventory_by_id


@router.get(
    "/inventories"
)
async def get_all_inventories(
        uow: UOWDep
):
    inventories = await InventoriesService.get_all_inventories(uow)
    return inventories

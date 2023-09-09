from schemas.inventories import InventoriesSchemaAdd
from utils.unit_of_work import IUnitOfWork


class InventoriesService:

    async def add_inventory(uow: IUnitOfWork, inventory: InventoriesSchemaAdd) -> int:
        async with uow:
            inventory_dict = inventory.model_dump()
            inventory_id = await uow.inventory.add_one(inventory_dict)
            await uow.commit()
            return inventory_id

    async def get_all_inventories(uow: IUnitOfWork):
        async with uow:
            inventories = await uow.inventory.find_all()
            return inventories

    async def get_inventories_by_id(uow: IUnitOfWork, inventory_id: int):
        async with uow:
            inventory_by_id = await uow.inventory.find_one(id=inventory_id)
            return inventory_by_id

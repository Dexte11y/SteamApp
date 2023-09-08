from schemas.inventories import InventoriesSchemaAdd
from utils.unit_of_work import IUnitOfWork


class InventoriesServece:

    # async def add_account(uow: IUnitOfWork, account: InventoriesSchemaAdd) -> int:
    #     async with uow:
    #         accounts_dict = account.model_dump()
    #         account_id = await uow.account.add_one(accounts_dict)
    #         await uow.commit()
    #         return account_id
    #
    # async def get_all_inventories(uow: IUnitOfWork):
    #     async with uow:
    #         accounts = await uow.account.find_all()
    #         return accounts

    async def get_inventories_by_id(uow: IUnitOfWork, inventory_id: int):
        async with uow:
            inventory_by_id = await uow.inventory.find_one(id=inventory_id)
            return inventory_by_id

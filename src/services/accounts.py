from schemas.accounts import AccountsSchemaAdd
from utils.unit_of_work import IUnitOfWork


class AccountsService:
    async def add_account(uow: IUnitOfWork, account: AccountsSchemaAdd) -> int:
        async with uow:
            accounts_dict = account.model_dump()
            account_id = await uow.account.add_one(accounts_dict)
            await uow.commit()
            return account_id

    async def get_all_accounts(uow: IUnitOfWork):
        async with uow:
            accounts = await uow.account.find_all()
            return accounts

    async def get_accounts_by_id(uow: IUnitOfWork, account_id: int):
        async with uow:
            accounts_by_id = await uow.account.find_one(id=account_id)
            return accounts_by_id

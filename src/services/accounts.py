from schemas.account import AccountsSchemaAdd
from utils.repository import AbstractRepository


class AccountsService:
    def __init__(self, accounts_repo: AbstractRepository):
        self.accounts_repo: AbstractRepository = accounts_repo()

    async def add_account(self, account: AccountsSchemaAdd):
        accounts_dict = account.model_dump()
        account_id = await self.accounts_repo.add_one(accounts_dict)
        return account_id

    async def get_all_accounts(self):
        accounts = await self.accounts_repo.find_all()
        return accounts

    async def get_accounts_by_id(self, account_id: int):
        accounts_by_id = await self.accounts_repo.find_one(id=account_id)
        return accounts_by_id

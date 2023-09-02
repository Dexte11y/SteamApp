from fastapi import APIRouter
from api.dependencies import UOWDep
from schemas.account import AccountsSchemaAdd
from services.accounts import AccountsService

router = APIRouter(
    prefix="/v1/accounts",
    tags=["Accounts"]
)


@router.post(
    ""
)
async def add_account(
        account: AccountsSchemaAdd,
        uow: UOWDep
):
    account_id = await AccountsService.add_account(uow, account)
    return {"account_id": account_id}


@router.get(
    ""
)
async def get_all_accounts(
        uow: UOWDep
):
    accounts = await AccountsService.get_all_accounts(uow)
    return accounts


@router.get(
    "/{id}"
)
async def get_accounts_by_id(
        account_id: int,
        uow: UOWDep
):
    account_by_id = await AccountsService.get_accounts_by_id(uow, account_id)
    return account_by_id


@router.get(
    "/inventories"
)
async def get_inventories(
        uow: UOWDep
):
    pass

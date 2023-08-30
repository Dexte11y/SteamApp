from fastapi import APIRouter, Depends
from typing_extensions import Annotated
from api.dependencies import accounts_service
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
        account_service: Annotated[AccountsService, Depends(accounts_service)]
):
    account_id = await account_service.add_account(account)
    return {"account_id": account_id}


@router.get(
    ""
)
async def get_all_accounts(
        account_service: Annotated[AccountsService, Depends(accounts_service)]
):
    accounts = await account_service.get_all_accounts()
    return accounts


@router.get(
    "/{id}"
)
async def get_accounts_by_id(
        account_id: int,
        account_service: Annotated[AccountsService, Depends(accounts_service)]
):
    account_by_id = await account_service.get_accounts_by_id(account_id)
    return account_by_id

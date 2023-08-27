from fastapi import APIRouter, Depends
from typing_extensions import Annotated
from api.dependencies import accounts_service
from schemas.account import AccountsSchemaAdd
from services.accounts import AccountsService

router = APIRouter(
    prefix="/accounts",
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
async def get_accounts(
        account_service: Annotated[AccountsService, Depends(accounts_service)]
):
    accounts = await account_service.get_accounts()
    return accounts

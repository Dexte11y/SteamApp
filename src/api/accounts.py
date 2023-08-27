from fastapi import APIRouter, Depends
from typing_extensions import Annotated
from dependencies import accounts_service

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
        accounts_service: Annotated[AccountsService, Depends(accounts_service)]
):
    account_id = await accounts_service.add_account(account)
    return {"task_id": account_id}


@router.get(
    ""
)
async def get_accounts(
        accounts_service: Annotated[AccountsService, Depends(accounts_service)]
):
    accounts = await accounts_service.get_accounts()
    return accounts

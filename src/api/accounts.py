from fastapi import APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

import models.accounts
from db.db import get_async_session
from models.accounts import Accounts
from schemas.account import AccountsSchemasBase

router = APIRouter(
    prefix="/accounts",
    tags=["Accounts"]
)


@router.post(
    ""
)
async def add_account(new_account: AccountsSchemasBase, session: AsyncSession = Depends(get_async_session)):
    account_dict = new_account.model_dump()
    stmt = insert(Accounts).values(**account_dict)
    # stmt = models.accounts.Accounts(**account_dict)
    session.add(stmt)
    await session.commit()
    return {"status": "success"}


@router.get(
    ""
)
async def get_user():
    pass

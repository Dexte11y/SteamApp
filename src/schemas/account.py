from datetime import date

from pydantic import BaseModel, ConfigDict


class AccountsSchemasBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    id_inventory: int
    name: str
    last_activity: date
    registration_date: date
    email: str
    phone: str
    steam_id: str


class AccountsSchemasAdd(AccountsSchemasBase):
    pass


class AccountsSchemasInDb(AccountsSchemasBase):
    pass

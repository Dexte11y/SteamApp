from datetime import date

from pydantic import BaseModel, ConfigDict


class AccountsSchemaBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    addressInventory: int
    name: str
    lastActivity: date
    registrationDate: date
    email: str
    phone: str
    idSteam: str
    idInventory: int


class AccountsSchemaAdd(AccountsSchemaBase):
    pass


class AccountsSchemaInDb(AccountsSchemaBase):
    pass

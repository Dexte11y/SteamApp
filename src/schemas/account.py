from datetime import date

from pydantic import BaseModel, ConfigDict


class AccountsSchemaBase(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    idInventory: int
    name: str
    lastActivity: date
    registrationDate: date
    email: str
    phone: str
    idSteam: str


class AccountsSchemaAdd(AccountsSchemaBase):
    pass


class AccountsSchemaInDb(AccountsSchemaBase):
    pass

from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.account import AccountsSchemaInDb


class Accounts(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    idInventory: Mapped[int]
    name: Mapped[str]
    lastActivity: Mapped[date]
    registrationDate: Mapped[date]
    email: Mapped[str]
    phone: Mapped[str]
    idSteam: Mapped[str]

    def to_read_model(self) -> AccountsSchemaInDb:
        return AccountsSchemaInDb(
            id=self.id,
            idInventory=self.idInventory,
            name=self.name,
            lastActivity=self.lastActivity,
            registrationDate=self.registrationDate,
            email=self.email,
            phone=self.phone,
            idSteam=self.idSteam
        )

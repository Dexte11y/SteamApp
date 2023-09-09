from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.db import Base
from models.inventories import Inventories
from schemas.accounts import AccountsSchemaInDb


class Accounts(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    addressInventory: Mapped[int]
    name: Mapped[str]
    lastActivity: Mapped[date]
    registrationDate: Mapped[date]
    email: Mapped[str]
    phone: Mapped[str]
    idSteam: Mapped[str]

    # idInventory: Mapped[int] = mapped_column(ForeignKey("inventories.id"))
    # inventoryItem: Mapped['Inventories'] = relationship(backref="accounts", uselist=False, lazy="joined")

    def to_read_model(self) -> AccountsSchemaInDb:
        return AccountsSchemaInDb(
            id=self.id,
            addressInventory=self.addressInventory,
            name=self.name,
            lastActivity=self.lastActivity,
            registrationDate=self.registrationDate,
            email=self.email,
            phone=self.phone,
            idSteam=self.idSteam,
            # idInventory=self.idInventory,
            # inventoryItem=self.inventoryItem.to_read_model(),
        )

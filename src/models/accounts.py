from datetime import date

from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.account import AccountsSchemaBase


class Accounts(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_inventory: Mapped[int]
    name: Mapped[str]
    last_activity: Mapped[date]
    registration_date: Mapped[date]
    email: Mapped[str]
    phone: Mapped[str]
    steam_id: Mapped[str]

    def to_read_model(self) -> AccountsSchemaBase:
        return AccountsSchemaBase(
            id=self.id,
            id_inventory=self.id_inventory,
            name=self.name,
            last_activity=self.last_activity,
            registration_date=self.registration_date,
            email=self.email,
            phone=self.phone,
            steam_id=self.steam_id,
        )

from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.accounts import AccountsSchemaInDb


class Inventories(Base):
    __tablename__ = "inventories"

    id: Mapped[int] = mapped_column(primary_key=True)
    item: Mapped[str]

    def to_read_model(self) -> AccountsSchemaInDb:
        return AccountsSchemaInDb(
            id=self.id,
            item=self.item,
        )

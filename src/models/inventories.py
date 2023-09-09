from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.inventories import InventoriesSchemaInDb


class Inventories(Base):
    __tablename__ = "inventories"

    id: Mapped[int] = mapped_column(primary_key=True)
    inventoryItem: Mapped[str]

    def to_read_model(self) -> InventoriesSchemaInDb:
        return InventoriesSchemaInDb(
            id=self.id,
            inventoryItem=self.inventoryItem,
        )

from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base


class Users(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    id_inventory: Mapped[int]
    name:Mapped[str]
    last_activity:Mapped[datetime]
    registration_date:Mapped[datetime]
    email:Mapped[str]
    phone:Mapped[str]
    steam_id: Mapped[str]

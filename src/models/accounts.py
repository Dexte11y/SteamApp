from datetime import date

from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base, engine


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


users_db = [
    {
        "id": 1,
        "id_inventory": 1,
        "name": "SusanWay",
        "last_activity": "2012-04-21T18:25:43-05:00",
        "registration_date": "2019-08-27T18:25:43-05:00",
        "email": "SusanWay@mail.ru",
        "phone": "89601578961",
        "steam_id": "76561198103854958"
    },
    {
        "id": 2,
        "id_inventory": 2,
        "name": "FinnKors",
        "last_activity": "2012-04-21T18:25:43-05:00",
        "registration_date": "2013-12-27T18:25:43-05:00",
        "email": "FinnKors@mail.ru",
        "phone": "89601578961",
        "steam_id": "76561198103854958"
    },
    {
        "id": 3,
        "id_inventory": 3,
        "name": "Dexte11y",
        "last_activity": "2014-07-14T18:25:43-05:00",
        "registration_date": "2015-06-13T18:25:43-05:00",
        "email": "Dexte11y@mail.ru",
        "phone": "89601578961",
        "steam_id": "76561198103854958"
    }
]

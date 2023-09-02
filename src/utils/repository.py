from abc import ABC, abstractmethod

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


class IRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError


class SQLAlchemyRepositoryImplementation(IRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_one(self, data: dict) -> int:
        stmt = (
            insert(self.model).
            values(**data).
            returning(self.model.id))
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def find_one(self, **kwargs):
        stmt = select(self.model).filter_by(**kwargs)
        res = await self.session.execute(stmt)
        return res.scalar_one().to_read_model()

    async def find_all(self):
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return [res[0].to_read_model() for res in result.all()]


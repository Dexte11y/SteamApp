from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from typing_extensions import AsyncGenerator


engine = create_async_engine("sqlite+aiosqlite:///spb_hub.db")
async_session_maker = async_sessionmaker(engine, class_=AsyncSession ,expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


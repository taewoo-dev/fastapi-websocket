from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database.connection_async import get_async_db
from app.user.models.user import User


class UserRepository:
    def __init__(self, db: AsyncSession = Depends(get_async_db)):
        self.db = db

    async def save(self, user: User) -> None:
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)

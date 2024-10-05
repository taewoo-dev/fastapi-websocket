from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.chat.models.room import Room
from core.database.connection_async import get_async_db


class RoomRepository:
    def __init__(self, db: AsyncSession = Depends(get_async_db)):
        self.db = db

    async def save(self, room: Room) -> None:
        self.db.add(room)
        await self.db.commit()

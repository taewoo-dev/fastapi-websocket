from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.chat.models.message import Message
from core.database.connection_async import get_async_db


class MessageRepository:
    def __init__(self, db: AsyncSession = Depends(get_async_db)):
        self.db = db

    async def save(self, message: Message) -> None:
        self.db.add(message)
        await self.db.commit()

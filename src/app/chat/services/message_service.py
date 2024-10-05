from fastapi import Depends

from app.chat.models.message import Message
from app.chat.repositorys.message_repository import MessageRepository


class MessageService:
    def __init__(self, repo: MessageRepository = Depends()):
        self.message_repo = repo

    async def save_message(self, room_id: str, user_id: int, content: str):
        message: Message = Message.create(
            content=content, room_id=room_id, user_id=user_id
        )
        await self.message_repo.save(message=message)

        return message

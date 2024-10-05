from fastapi import Depends

from app.chat.models.room import Room
from app.chat.repositorys.room_repository import RoomRepository


class RoomService:
    def __init__(self, repo: RoomRepository = Depends()):
        self.room_repo = repo

    async def save_room(self, room_name):
        room: Room = Room.create(name=room_name)

        await self.room_repo.save(room=room)

        return room

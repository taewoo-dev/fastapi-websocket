from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from common.models.base import AbstractBaseClass


class Message(AbstractBaseClass):
    __tablename__ = "messages"

    content = Column(String(500), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)

    sender = relationship("User", back_populates="messages")
    room = relationship("Room", back_populates="messages")

    def __repr__(self):
        return f"<Message(content={self.content}, sender_id={self.sender_id}, room_id={self.room_id})>"

    @classmethod
    def create(cls, content: str, room_id: str, user_id: int):
        return cls(content=content, sender_id=user_id, room_id=room_id)

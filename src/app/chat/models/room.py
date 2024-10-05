from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from common.models.base import AbstractBaseClass  # AbstractBaseClass 가져오기


class Room(AbstractBaseClass):  # 이제 AbstractBaseClass만 상속받으면 됨
    __tablename__ = "rooms"

    name = Column(String(255), index=True)  # 채팅방 이름
    messages = relationship("Message", back_populates="room")

    @classmethod
    def create(cls, name: str):
        return cls(name=name)

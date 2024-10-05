from sqlalchemy import String, Column
from sqlalchemy.orm import relationship

from common.models.base import AbstractBaseClass


class User(AbstractBaseClass):  # 예시 사용자 모델
    __tablename__ = "users"

    name = Column(String(20), index=True)
    messages = relationship("Message", back_populates="sender")  # 메시지와의 관계 설정

    @classmethod
    def create(cls, name: str):
        return cls(name=name)

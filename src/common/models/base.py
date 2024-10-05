from sqlalchemy import Column, Date, Time, Integer
from core.database.orm import Base
from datetime import datetime


class AbstractBaseClass(Base):
    __abstract__ = True  # SQLAlchemy에서 추상 클래스임을 명시

    id = Column(Integer, primary_key=True, index=True)
    create_date = Column(Date, default=datetime.utcnow().date)
    create_time = Column(Time, default=datetime.utcnow().time)
    update_date = Column(
        Date, default=datetime.utcnow().date, onupdate=lambda: datetime.utcnow().date()
    )
    update_time = Column(
        Time, default=datetime.utcnow().time, onupdate=lambda: datetime.utcnow().time()
    )

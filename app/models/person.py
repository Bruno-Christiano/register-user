from sqlalchemy import Column, Integer, String, DateTime
from db.base import Base
from sqlalchemy.sql import func


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(
        DateTime, default=func.now(), onupdate=func.now(), nullable=False
    )
    enrolment = Column(Integer, nullable=False, unique=True)

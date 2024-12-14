from sqlalchemy import Column, Integer, LargeBinary, TypeDecorator
from sqlalchemy.orm import Mapped

from src.database import Base


class ListType(TypeDecorator):
    impl = LargeBinary

    def process_bind_param(self, value: list[int], dialect):
        return bytes(value)

    def process_result_value(self, value: bytes, dialect):
        return list(value)


class ImageORM(Base):
    __tablename__ = "images"

    id: Mapped[int] = Column(Integer, primary_key=True)
    data: Mapped[list[int]] = Column(ListType)

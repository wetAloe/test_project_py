from sqlalchemy import Column, Integer, LargeBinary
from sqlalchemy.orm import Mapped

from src.database import Base


class ImageORM(Base):
    __tablename__ = "images"

    id: Mapped[int] = Column(Integer, primary_key=True)
    data: Mapped[bytes] = Column(LargeBinary)

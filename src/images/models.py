from sqlalchemy import Column, Integer, ARRAY

from database import Base


class ImageORM(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    data = Column(ARRAY(Integer))

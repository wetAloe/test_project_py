from sqlmodel import ARRAY, Field, Integer, SQLModel
from pydantic import field_validator


class Image(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    data: list[int] = Field(sa_type=ARRAY(Integer))

    @field_validator("data")
    @classmethod
    def check_image_length(cls, v):
        if len(v) == 0:
            raise ValueError("Image data cannot be empty")
        return v

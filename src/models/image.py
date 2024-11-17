from sqlmodel import ARRAY, Field, Integer, SQLModel


class Image(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    data: list[int] = Field(sa_type=ARRAY(Integer))

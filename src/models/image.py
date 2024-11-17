from sqlmodel import Field, SQLModel, ARRAY, Integer


class Image(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    data: list[int] = Field(sa_type=ARRAY(Integer))

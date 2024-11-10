from sqlalchemy import Column, Integer, ARRAY, MetaData, Table


metadata = MetaData()

images_table = Table(
    "images",
    metadata,
    Column("depth", Integer, primary_key=True, autoincrement=True),
    Column("data", ARRAY(Integer)),
)

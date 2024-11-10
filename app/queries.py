from models import metadata


def create_tables(engine):
    metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)

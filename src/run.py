import uvicorn

from app import create_app
from settings import get_app_settings


def run():
    app = create_app()
    settings = get_app_settings()
    uvicorn.run(app, host=settings.host, port=settings.port)


if __name__ == "__main__":
    run()

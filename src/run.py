import uvicorn

from src.app import create_app
from src.settings import RuntimeSettings


def run():
    app = create_app()
    settings = RuntimeSettings()
    uvicorn.run(app, host=settings.host, port=settings.port)


if __name__ == "__main__":
    run()

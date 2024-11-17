import uvicorn

from app import create_app


def run():
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run()

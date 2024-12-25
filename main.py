import asyncio
import uvicorn
from fastapi import FastAPI

from database.orm.methods import create_tables
from routers.api import api_router
from config import settings


def create_fastapi_app():
    fastapi_app = FastAPI()

    fastapi_app.include_router(api_router, prefix="/api")

    return fastapi_app

app = create_fastapi_app()

async def main():
    create_tables()


if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run(
        app="main:app",
        reload=True,
        host=settings.uvicorn_host,
        port=settings.uvicorn_port,
    )


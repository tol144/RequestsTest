from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config import settings


sync_engine = create_engine(
    settings.get_sync_url,
    echo=True,
)

async_engine = create_async_engine(
    settings.get_async_url,
    echo=True,
)

sync_session = sessionmaker(sync_engine, expire_on_commit=False)
async_session = async_sessionmaker(async_engine, expire_on_commit=False)

from database.engine import sync_engine
from database.connection import async_orm_connection
from database.orm.model import BaseModel, RequestResults


def create_tables():
    BaseModel.metadata.create_all(sync_engine)


@async_orm_connection
async def insert(data_list, session):
    session.add_all(data_list)
    await session.commit()


async def insert_request_result(result: str):
    await insert([RequestResults(result=result)])

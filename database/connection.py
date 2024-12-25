from database.engine import async_session, sync_session, async_engine


def orm_connection(method):
    async def wrapper(*args, **kwargs):
        with sync_session() as session:
            try:
                return method(*args, session=session, **kwargs)
            except Exception as e:
                session.rollback()
                raise e
            finally:
                session.close()

    return wrapper

def async_orm_connection(method):
    async def wrapper(*args, **kwargs):
        async with async_session() as session:
            try:
                return await method(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()

    return wrapper


def async_engine_connection(method):
    async def wrapper(*args, **kwargs):
        async with async_engine.connect() as connection:
            try:
                return await method(*args, connection=connection, **kwargs)
            except Exception as e:
                await connection.rollback()
                raise e
            finally:
                await connection.close()

    return wrapper

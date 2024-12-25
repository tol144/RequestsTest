from fastapi import APIRouter

from database.orm.methods import insert_request_result


api_router = APIRouter()


@api_router.post("/save_data")
async def create_new_order(**kwargs):
    await insert_request_result(str(kwargs))

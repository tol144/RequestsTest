from fastapi import APIRouter, Request

from database.orm.methods import insert_request_result
from typing import List


api_router = APIRouter()


@api_router.post("/save_json")
async def create_new_order(data: dict):
    await insert_request_result(str(data))


@api_router.post("/save_data")
async def create_new_order(request: Request):
    request_data = await request.form()
    data = {key: value for key, value in request_data.items()}
    await insert_request_result(str(data))

from fastapi import APIRouter

from api.users.schema import (
    UserCreateRequest
)

from api.users import utility


router = APIRouter(
    tags=["Users"]
)

@router.post("/users")
async def create_user(
    payload: UserCreateRequest
):

    return await (
        utility.create_user(
            payload.model_dump()
        )
    )

@router.get("/users")
async def get_users():

    return await (
        utility.get_users()
    )

@router.post(
    "/jobs/user-expire"
)
async def user_expire():

    return await (
        utility.expire_users()
    )

@router.post(
    "/jobs/user-disable"
)
async def user_disable():

    return await (
        utility.disable_users()
    )
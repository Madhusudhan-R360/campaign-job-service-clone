from fastapi import APIRouter

from api.orders.schema import (
    OrderCreateRequest
)

from api.orders import utility


router = APIRouter(
    tags=["Orders"]
)

@router.post("/orders")
async def create_order(
    payload: OrderCreateRequest
):

    return await (
        utility.create_order(
            payload.model_dump()
        )
    )

@router.get("/orders")
async def get_orders():

    return await (
        utility.get_orders()
    )

@router.get(
    "/orders/{order_id}"
)
async def get_order(
    order_id: str
):

    return await (
        utility.get_order(
            order_id
        )
    )

@router.post(
    "/jobs/reconcile-orders"
)
async def reconcile_orders():

    return await (
        utility.reconcile_orders()
    )
from datetime import datetime
import uuid

from db.connection import (
    orders_collection,
    voucher_collection
)

async def create_order(
    data: dict
):

    payload = {
        **data,
        "status": "PENDING",
        "voucher_code": None,
        "created_at":
        datetime.utcnow()
    }

    await orders_collection.insert_one(
        payload
    )

    return {
        "success": True,
        "message":
        "Order Created"
    }

async def get_orders():

    orders = await (
        orders_collection
        .find()
        .to_list(None)
    )

    for order in orders:
        order["_id"] = str(order["_id"])

    return orders

async def get_order(
    order_id: str
):

    order = await (
        orders_collection.find_one(
            {
                "order_id":
                order_id
            }
        )
    )

    if order:
        order["_id"] = str(order["_id"])

    return order

async def reconcile_orders():

    pending_orders = await (
        orders_collection
        .find(
            {
                "status":
                "PENDING"
            }
        )
        .to_list(None)
    )

    processed_count = 0

    for order in pending_orders:

        voucher_code = (
            str(uuid.uuid4())[:8]
            .upper()
        )

        await voucher_collection.insert_one(
            {
                "order_id":
                order["order_id"],
                "voucher_code":
                voucher_code,
                "created_at":
                datetime.utcnow()
            }
        )

        await orders_collection.update_one(
            {
                "_id":
                order["_id"]
            },
            {
                "$set":
                {
                    "status":
                    "COMPLETED",
                    "voucher_code":
                    voucher_code
                }
            }
        )

        processed_count += 1

    return {
        "success": True,
        "processed_orders":
        processed_count
    }
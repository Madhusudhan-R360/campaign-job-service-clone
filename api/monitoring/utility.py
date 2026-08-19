from datetime import datetime

from db.connection import (
    monitoring_collection,
    user_collection,
    orders_collection
)

async def monitor_system():

    active_users = await (
        user_collection.count_documents(
            {
                "status": "ACTIVE"
            }
        )
    )

    expired_users = await (
        user_collection.count_documents(
            {
                "status": "EXPIRED"
            }
        )
    )

    disabled_users = await (
        user_collection.count_documents(
            {
                "status": "DISABLED"
            }
        )
    )

    pending_orders = await (
        orders_collection.count_documents(
            {
                "status": "PENDING"
            }
        )
    )

    completed_orders = await (
        orders_collection.count_documents(
            {
                "status": "COMPLETED"
            }
        )
    )

    log = {
        "active_users":
        active_users,

        "expired_users":
        expired_users,

        "disabled_users":
        disabled_users,

        "pending_orders":
        pending_orders,

        "completed_orders":
        completed_orders,

        "generated_at":
        datetime.utcnow()
    }

    result = await (
    monitoring_collection.insert_one(
        log
    )
)

    log["_id"] = str(
    result.inserted_id
)

    return {
    "success": True,
    "data": log
}

async def get_monitoring_logs():

    logs = await (
        monitoring_collection
        .find()
        .to_list(None)
    )

    for log in logs:

        log["_id"] = str(
            log["_id"]
        )

    return logs

async def dashboard():

    return {
        "active_users":
        await user_collection.count_documents(
            {
                "status":
                "ACTIVE"
            }
        ),

        "expired_users":
        await user_collection.count_documents(
            {
                "status":
                "EXPIRED"
            }
        ),

        "disabled_users":
        await user_collection.count_documents(
            {
                "status":
                "DISABLED"
            }
        ),

        "pending_orders":
        await orders_collection.count_documents(
            {
                "status":
                "PENDING"
            }
        ),

        "completed_orders":
        await orders_collection.count_documents(
            {
                "status":
                "COMPLETED"
            }
        )
    }
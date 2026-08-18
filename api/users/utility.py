from datetime import datetime

from db.connection import (
    user_collection
)

async def create_user(
    data: dict
):

    payload = {
        **data,
        "status": "ACTIVE",
        "created_at":
        datetime.utcnow()
    }

    result = await (
        user_collection.insert_one(
            payload
        )
    )

    return {
        "success": True,
        "user_id":
        str(result.inserted_id)
    }

async def get_users():

    users = await (
        user_collection
        .find()
        .to_list(None)
    )

    for user in users:

        user["_id"] = str(
            user["_id"]
        )

    return users

async def expire_users():

    current_time = datetime.utcnow()

    result = await (
        user_collection.update_many(
            {
                "expiry_date":
                {
                    "$lt":
                    current_time
                },
                "status":
                "ACTIVE"
            },
            {
                "$set":
                {
                    "status":
                    "EXPIRED"
                }
            }
        )
    )

    return {
        "success": True,
        "expired_users":
        result.modified_count
    }

async def disable_users():

    result = await (
        user_collection.update_many(
            {
                "status":
                "EXPIRED"
            },
            {
                "$set":
                {
                    "status":
                    "DISABLED"
                }
            }
        )
    )

    return {
        "success": True,
        "disabled_users":
        result.modified_count
    }
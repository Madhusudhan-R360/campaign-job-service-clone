from datetime import datetime, timedelta
from db.connection import (
    reminders_collection,
    user_collection
)

async def create_reminder(
    data: dict
):

    payload = {
        **data,
        "status": "PENDING",
        "created_at": datetime.utcnow()
    }

    result = await (
        reminders_collection.insert_one(
            payload
        )
    )

    return {
        "success": True,
        "reminder_id":
        str(result.inserted_id)
    }

async def get_reminders():

    reminders = await (
        reminders_collection
        .find()
        .to_list(None)
    )

    for item in reminders:
        item["_id"] = str(item["_id"])

    return reminders

async def send_reminders():

    target_date = (
        datetime.utcnow() +
        timedelta(days=7)
    )

    users = await (
        user_collection.find(
            {
                "status": "ACTIVE"
            }
        ).to_list(None)
    )

    reminder_count = 0

    for user in users:

        expiry_date = (
            user["expiry_date"]
        )

        if expiry_date <= target_date:

            await (
                reminders_collection
                .insert_one(
                    {
                        "user_id":
                        user["user_id"],
                        "campaign_id":
                        user["campaign_id"],
                        "message":
                        "Your campaign benefit expires soon.",
                        "status":
                        "SENT",
                        "created_at":
                        datetime.utcnow()
                    }
                )
            )

            reminder_count += 1

    return {
        "success": True,
        "reminders_sent":
        reminder_count
    }
from fastapi import APIRouter

from api.reminders.schema import (
    ReminderCreateRequest
)

from api.reminders import utility


router = APIRouter(
    tags=["Reminders"]
)

@router.post(
    "/reminders"
)
async def create_reminder(
    payload: ReminderCreateRequest
):

    return await (
        utility.create_reminder(
            payload.model_dump()
        )
    )

@router.get(
    "/reminders"
)
async def get_reminders():

    return await (
        utility.get_reminders()
    )

@router.post(
    "/jobs/send-reminders"
)
async def send_reminders():

    return await (
        utility.send_reminders()
    )
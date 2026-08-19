from pydantic import BaseModel


class ReminderCreateRequest(
    BaseModel
):
    user_id: str
    campaign_id: str
    message: str
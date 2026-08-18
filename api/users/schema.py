from datetime import datetime

from pydantic import BaseModel


class UserCreateRequest(
    BaseModel
):
    user_id: str
    name: str
    email: str
    campaign_id: str
    expiry_date: datetime

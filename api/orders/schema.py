from pydantic import BaseModel


class OrderCreateRequest(
    BaseModel
):
    order_id: str
    user_id: str
    campaign_id: str
    amount: float
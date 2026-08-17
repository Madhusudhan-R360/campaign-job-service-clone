from pydantic import BaseModel


class AnalyticsRequest(
    BaseModel
):
    campaign_id: str
    campaign_name: str
    active_users: int
    expired_users: int
    total_orders: int
    transaction_volume: float
from pydantic import BaseModel


class MonitoringResponse(
    BaseModel
):
    active_users: int
    expired_users: int
    disabled_users: int
    pending_orders: int
    completed_orders: int
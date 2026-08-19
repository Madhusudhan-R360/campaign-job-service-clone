from fastapi import APIRouter

from api.monitoring import utility

router = APIRouter(
    tags=["Monitoring"]
)

@router.post(
    "/jobs/monitor-system"
)
async def monitor_system():

    return await (
        utility.monitor_system()
    )

@router.get(
    "/monitoring/dashboard"
)
async def dashboard():

    return await (
        utility.dashboard()
    )

@router.get(
    "/monitoring/logs"
)
async def logs():

    return await (
        utility.get_monitoring_logs()
    )
from fastapi import FastAPI

from api.analytics.app import (
    router as analytics_router
)

from api.users.app import (
    router as user_router
)

from api.orders.app import (
    router as order_router
)

from api.reminders.app import (
    router as reminder_router
)

app = FastAPI(
    title="Campaign Job Service Clone"
)

app.include_router(
    analytics_router
)

app.include_router(
    user_router
)

app.include_router(
    order_router
)

app.include_router(
    reminder_router
)

@app.get("/health")
async def health():

    return {
        "success": True
    }
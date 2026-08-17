from fastapi import FastAPI

from api.analytics.app import (
    router as analytics_router
)

app = FastAPI(
    title="Campaign Job Service Clone"
)

app.include_router(
    analytics_router
)

@app.get("/health")
async def health():

    return {
        "success": True
    }
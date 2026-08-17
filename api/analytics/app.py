from fastapi import APIRouter

from api.analytics.schema import (
    AnalyticsRequest
)

from api.analytics import utility


router = APIRouter(
    tags=["Analytics"]
)

@router.post(
    "/analytics/generate"
)
async def generate(
    data: AnalyticsRequest
):

    return await (
        utility.generate_analytics(
            data.model_dump()
        )
    )

@router.get(
    "/analytics"
)
async def get_all():

    return await (
        utility.get_analytics()
    )

@router.get(
    "/analytics/{campaign_id}"
)
async def get_campaign(
    campaign_id: str
):

    return await (
        utility.get_campaign_analytics(
            campaign_id
        )
    )
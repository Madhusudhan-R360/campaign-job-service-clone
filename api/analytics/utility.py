from datetime import datetime

from db.connection import (
    campaign_analytics_collection
)


async def generate_analytics(
    data: dict
):

    analytics_data = {
        **data,
        "generated_at":
        datetime.utcnow()
    }

    result = await (
        campaign_analytics_collection
        .insert_one(
            analytics_data
        )
    )

    return {
        "success": True,
        "analytics_id":
        str(
            result.inserted_id
        )
    }

async def get_analytics():

    analytics = await (
        campaign_analytics_collection
        .find()
        .to_list(None)
    )

    for item in analytics:

        item["_id"] = str(
            item["_id"]
        )

    return analytics

async def get_campaign_analytics(
    campaign_id: str
):

    data = await (
        campaign_analytics_collection
        .find(
            {
                "campaign_id":
                campaign_id
            }
        )
        .to_list(None)
    )

    for item in data:

        item["_id"] = str(
            item["_id"]
        )

    return data
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.models.road_condition_feature import RoadConditionFeature
from sqlalchemy import select

async def get_road_condition_features(ssesion: AsyncSession) -> list[RoadConditionFeature]:
    stmt = select(RoadConditionFeature).order_by(RoadConditionFeature.id)
    result = await ssesion.execute(stmt)
    road_condition_features = result.scalars().all()

    return list(road_condition_features)


async def get_road_condition_feature_by_id(
    session: AsyncSession, feature_id: str
) -> RoadConditionFeature | None:
    return await session.get(RoadConditionFeature, feature_id) 



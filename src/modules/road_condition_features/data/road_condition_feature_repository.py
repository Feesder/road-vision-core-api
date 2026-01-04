from sqlalchemy.ext.asyncio import AsyncSession
from src.common.models.road_condition_feature import RoadConditionFeature
from sqlalchemy import select
from src.modules.road_condition_features.dto.road_condition_feautre_dto import RoadConditionFeatureDto

async def get_road_condition_features(ssesion: AsyncSession) -> list[RoadConditionFeature]:
    stmt = select(RoadConditionFeature).order_by(RoadConditionFeature.id)
    result = await ssesion.execute(stmt)
    road_condition_features = result.scalars().all()

    return list(road_condition_features)


async def get_road_condition_feature_by_id(
    session: AsyncSession, feature_id: str
) -> RoadConditionFeature | None:
    return await session.get(RoadConditionFeature, feature_id) 

async def update_road_condition_feature(
    session: AsyncSession, payload: RoadConditionFeatureDto
) -> RoadConditionFeature:
    feature = RoadConditionFeature(**payload.dict())
    session.add(feature)
    await session.commit()
    await session.refresh(feature)
    return feature


async def delete_road_condition_feature(
    session: AsyncSession, feature: RoadConditionFeature
) -> None:
    await session.delete(feature)
    await session.commit()



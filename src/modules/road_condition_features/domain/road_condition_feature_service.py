from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import src.modules.road_condition_features.data.road_condition_feature_repository as road_condition_features_repository
from src.common.models.road_condition_feature import RoadConditionFeature
from fastapi import status
from src.common.constants.error_code import ErrorCode


async def get_road_condition_features(session: AsyncSession) -> list[RoadConditionFeature]:
    road_condition_features = await road_condition_features_repository.get_road_condition_features(session)

    return road_condition_features


async def get_road_condition_feature_by_id(
    session: AsyncSession, feature_id: str
) -> RoadConditionFeature | None:
    road_condition_feature = await road_condition_features_repository.get_road_condition_feature_by_id(
        session, feature_id
    )

    if (road_condition_feature is None):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ErrorCode.RoadConditionFeatureNotFound.value
        )

    return road_condition_feature


async def update_road_condition_feature(
    session: AsyncSession, payload: RoadConditionFeature
) -> RoadConditionFeature:
    road_condition_feature = road_condition_features_repository.get_road_condition_feature_by_id(session, payload.id)

    if road_condition_feature is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ErrorCode.RoadConditionFeatureNotFound.value
        )
    
    updated_road_condition_feature = await road_condition_features_repository.update_road_condition_feature(session, payload)

    return updated_road_condition_feature


async def delete_road_condition_feature(
    session: AsyncSession, feature: RoadConditionFeature
) -> None:
    road_condition_feature = road_condition_features_repository.get_road_condition_feature_by_id(session, feature.id)

    if road_condition_feature is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=ErrorCode.RoadConditionFeatureNotFound.value
        )
    
    await road_condition_features_repository.delete_road_condition_feature(session, feature)
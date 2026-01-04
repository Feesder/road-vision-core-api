from sqlalchemy.ext.asyncio import AsyncSession
import src.modules.road_condition_features.data.road_condition_feature_repository as road_condition_features_repository
from src.common.models.road_condition_feature import RoadConditionFeature


async def get_road_condition_features(session: AsyncSession) -> list[RoadConditionFeature]:
    road_condition_features = await road_condition_features_repository.get_road_condition_features(session)

    return road_condition_features


from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.common.database.db_helper import db_helper
from src.modules.road_condition_features.domain.road_condition_feature_service import get_road_condition_features
from fastapi import Depends
from src.common.mapper.users.road_condition_features_mapper import mapRoadConditionFeatureToRoadConditionFeatureDto


road_condition_feature_router = APIRouter(
    prefix="/api/v1/road-condition-features", tags=["road-condition-features"]
)


@road_condition_feature_router.post("")
async def create_road_condition_feature():
    pass


@road_condition_feature_router.get("")
async def get_road_condition_features(session: AsyncSession = Depends(db_helper.scoped_session_depedency)):
    road_condition_features = await get_road_condition_features(session)

    return list(map(mapRoadConditionFeatureToRoadConditionFeatureDto, road_condition_features))


@road_condition_feature_router.get("/{feature_id}")
async def get_road_condition_feature_by_id(feature_id: str):
    pass


@road_condition_feature_router.patch("/{feature_id}")
async def update_road_condition_feature(feature_id: str):
    pass


@road_condition_feature_router.delete("/{feature_id}")
async def delete_road_condition_feature(feature_id: str):
    pass

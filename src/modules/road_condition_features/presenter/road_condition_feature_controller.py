from fastapi import APIRouter


road_condition_feature_router = APIRouter(prefix="/api/v1/road-condition-features", tags=["road-condition-features"])


@road_condition_feature_router.post("")
async def create_road_condition_feature():
    pass

@road_condition_feature_router.get("")
async def get_road_condition_features():
    pass

@road_condition_feature_router.get("/{feature_id}")
async def get_road_condition_feature_by_id(feature_id: str):
    pass

@road_condition_feature_router.patch("/{feature_id}")
async def update_road_condition_feature(feature_id: str):
    pass

@road_condition_feature_router.delete("/{feature_id}")
async def delete_road_condition_feature(feature_id: str):
    pass
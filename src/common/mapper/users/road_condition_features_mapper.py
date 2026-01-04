from src.common.models.road_condition_feature import RoadConditionFeature
from src.modules.road_condition_features.dto.road_condition_feautre_dto import (
    RoadConditionFeatureDto,
)

def mapRoadConditionFeatureToRoadConditionFeatureDto(road_condition_features: RoadConditionFeature): 
    return RoadConditionFeatureDto(
        longitude=road_condition_features.longitude,
        latitude=road_condition_features.latitude,
        accuracy=road_condition_features.accuracy,
        road_type=road_condition_features.road_type,
    )
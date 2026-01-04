from pydantic import BaseModel
from common.constants.road_type import RoadType
from typing import Optional


class RoadConditionFeatureCreate(BaseModel):
    road_type: RoadType
    latitude: float
    longitude: float
    accuracy: float


class RoadConditionFeatureUpdate(BaseModel):
    road_type: Optional[RoadType] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    accuracy: Optional[float] = None
from dataclasses import dataclass


@dataclass
class RoadConditionFeatureDto:
    longitude: float
    latitude: float
    accuracy: float
    road_type: str
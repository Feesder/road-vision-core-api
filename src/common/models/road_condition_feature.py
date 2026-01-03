from sqlalchemy.orm import Mapped, mapped_column
from src.common.models.base import Base
from src.common.constants.road_type import RoadType
from sqlalchemy import Enum


class RoadConditionFeature(Base):
    __tablename__ = "road_condition_features"

    longitude: Mapped[float] = mapped_column(nullable=False)
    latitude: Mapped[float] = mapped_column(nullable=False)
    accuracy: Mapped[float] = mapped_column(nullable=False)
    road_condition: Mapped[RoadType] = mapped_column(
        Enum(RoadType, name="road_condition", native_enum=True), nullable=False
    )

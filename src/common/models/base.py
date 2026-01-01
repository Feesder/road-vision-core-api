from datetime import datetime
import uuid
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[str] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)

    created_at: Mapped[datetime] = mapped_column(insert_default=func.now(), nullable=False, server_default=func.now())

    updated_at: Mapped[datetime] = mapped_column(
        insert_default=func.now(), onupdate=func.now(), server_default=func.now(), nullable=False
    )

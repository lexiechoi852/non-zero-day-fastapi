import uuid
from datetime import datetime, timezone
from decimal import Decimal
from typing import List, TYPE_CHECKING

from sqlalchemy import String, Numeric
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP
from sqlmodel import SQLModel, Field, Column, Relationship

if TYPE_CHECKING:
    from app.models.habit_log import HabitLog

class Action(SQLModel, table=True):
    __tablename__ = "actions"

    id: uuid.UUID = Field(sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    habit_id: uuid.UUID = Field(foreign_key="habits.id", nullable=False)
    label: str = Field(sa_column=Column(String(100), nullable=False))
    value: Decimal = Field(sa_column=Column(Numeric(3, 2), nullable=False))
    created_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False),
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False),
        default_factory=lambda: datetime.now(timezone.utc)
    )

    habit: "Habit" = Relationship(back_populates="actions")
    habit_logs: List[HabitLog] = Relationship(back_populates="action")

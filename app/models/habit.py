import uuid
from datetime import datetime, timezone
from typing import List, TYPE_CHECKING

from sqlalchemy import Column, Text, String, TIMESTAMP, Boolean, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from app.models.action import Action
    from app.models.habit_log import HabitLog
    from app.models.habit_streak import HabitStreak

class Habit(SQLModel, table=True):
    __tablename__ = "habits"

    id: uuid.UUID = Field(sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    user_id: uuid.UUID = Field(foreign_key="users.id", nullable=False)
    name: str = Field(sa_column=Column(String(100), nullable=False))
    description: str | None = Field(default=None, sa_column=Column(Text, nullable=True))
    sort_order: int = Field(sa_column=Column(Integer, nullable=False))
    is_archived: bool = Field(sa_column=Column(Boolean, nullable=False, default=False))
    archived_at: datetime | None = Field(
        default=None,
        sa_column=Column(TIMESTAMP(timezone=True), nullable=True)
    )
    created_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False),
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            default=lambda: datetime.now(timezone.utc),
            onupdate=lambda: datetime.now(timezone.utc),
        )
    )

    user: "User" = Relationship(back_populates="habits")
    actions: List[Action] = Relationship(back_populates="habit")
    habit_logs: List[HabitLog] = Relationship(back_populates="habit")
    habit_streaks: List[HabitStreak] = Relationship(back_populates="habit")
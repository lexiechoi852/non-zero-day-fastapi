from datetime import datetime, timezone
import uuid
from typing import List, TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID, TIMESTAMP


if TYPE_CHECKING:
    from app.models.habit import Habit
    from app.models.habit_log import HabitLog
    from app.models.habit_streak import HabitStreak

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    display_name: str = Field(sa_column=Column(String(100), nullable=False))
    email: str = Field(sa_column=Column(String(100), unique=True, nullable=False))
    password: str = Field(sa_column=Column(String(100), nullable=False))
    timezone: str = Field(sa_column=Column(String(50), nullable=False))
    created_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False),
        default_factory=lambda: datetime.now(timezone.utc)
    )
    updated_at: datetime = Field(
        sa_column=Column(TIMESTAMP(timezone=True), nullable=False),
        default_factory=lambda: datetime.now(timezone.utc)
    )

    habits: List[Habit] = Relationship(back_populates="user")
    habit_logs: List[HabitLog] = Relationship(back_populates="user")
    habit_streaks: List[HabitStreak] = Relationship(back_populates="user")
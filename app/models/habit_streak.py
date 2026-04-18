import uuid
from datetime import date, datetime, timezone

from sqlalchemy import Column, UUID, Integer, Date, TIMESTAMP
from sqlmodel import SQLModel, Field, Relationship


class HabitStreak(SQLModel, table=True):
    __tablename__ = "habit_streaks"

    id: uuid.UUID = Field(sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    user_id: uuid.UUID = Field(foreign_key="users.id", nullable=False)
    habit_id: uuid.UUID = Field(foreign_key="habits.id", nullable=False)
    current_streak: int = Field(sa_column=Column(Integer, default=0, nullable=False))
    longest_streak: int = Field(sa_column=Column(Integer, default=0, nullable=False))
    last_logged_date: date | None = Field(sa_column=Column(Date, nullable=True))
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

    user: "User" = Relationship(back_populates="habit_streaks")
    habit: "Habit" = Relationship(back_populates="habit_streaks")

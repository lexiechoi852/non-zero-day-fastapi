import uuid
from decimal import Decimal
from datetime import date, datetime, timezone

from sqlalchemy import Column, Numeric, Date, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlmodel import SQLModel, Field, Relationship


class HabitLog(SQLModel, table=True):
    __tablename__ = "habit_logs"

    id: uuid.UUID = Field(sa_column=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4))
    user_id: uuid.UUID = Field(foreign_key="users.id", nullable=False)
    habit_id: uuid.UUID = Field(foreign_key="habits.id", nullable=False)
    action_id: uuid.UUID = Field(foreign_key="actions.id", nullable=False)
    value: Decimal = Field(sa_column=Column(Numeric(3, 2), nullable=False))
    log_date: date = Field(sa_column=Column(Date, nullable=False))
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

    user: "User" = Relationship(back_populates="habit_logs")
    habit: "Habit" = Relationship(back_populates="habit_logs")
    action: "Action" = Relationship(back_populates="habit_logs")


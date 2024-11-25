from sqlalchemy import Column, ForeignKey, String, Table

from .base import Base


user_meal_association = Table(
    "user_meal_association",
    Base.metadata,
    Column("user_id", String(36), ForeignKey("users.id"), primary_key=True),
    Column("meal_id", String(36), ForeignKey("meals.id"), primary_key=True),
)

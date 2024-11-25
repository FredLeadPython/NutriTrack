from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .association_table import user_meal_association
from .base import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=True)

    meals = relationship(
        "MealModel", secondary=user_meal_association, back_populates="users"
    )

import enum
import uuid

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import Base
from .user_model import user_meal_association


class MealType(enum.Enum):
    BREAKFAST = "Breakfast"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    SNACK = "Snack"


class DietaryPreferences(enum.Enum):
    VEGETARIAN = "Vegetarian"
    VEGAN = "Vegan"
    GLUTEN_FREE = "Gluten-Free"
    NONE = "None"


class Allergens(enum.Enum):
    DAIRY = "Dairy"
    GLUTEN = "Gluten"
    NUTS = "Nuts"
    SOY = "Soy"
    NONE = "None"


class MealModel(Base):
    __tablename__ = "meals"
    id = Column(
        String,
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    type = Column(String, nullable=False)
    dietary_preferences = Column(String, nullable=False)
    allergens = Column(String, nullable=False)

    users = relationship(
        "UserModel", secondary=user_meal_association, back_populates="meals"
    )

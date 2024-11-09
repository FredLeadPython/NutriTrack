from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from nutritrack.app.config import Base
from nutritrack.app.models.meal import meal_food  # Importez la table de liaison

class Food(Base):
    __tablename__ = "food"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    calories = Column(Integer, nullable=False)
    proteins = Column(Float, nullable=False)
    carbohydrates = Column(Float, nullable=False)
    fats = Column(Float, nullable=False)
    vitamins = Column(String)

    # Relation avec Meal via la table de liaison
    meals = relationship("Meal", secondary=meal_food, back_populates="foods")

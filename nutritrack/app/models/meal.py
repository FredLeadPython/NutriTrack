from sqlalchemy import Column, Integer, ForeignKey, Date, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from nutritrack.app.config import Base


meal_food = Table(
    "meal_food",
    Base.metadata,
    Column("meal_id", Integer, ForeignKey("meals.id"), primary_key=True),
    Column("food_id", Integer, ForeignKey("food.id"), primary_key=True),
)

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Clé étrangère vers User
    date = Column(Date, nullable=False)
    total_calories = Column(Float, nullable=False)
    total_proteins = Column(Float, nullable=False)
    total_carbohydrates = Column(Float, nullable=False)
    total_fats = Column(Float, nullable=False)

    foods = relationship("Food", secondary=meal_food, back_populates="meals")
    user = relationship("User", back_populates="meals")
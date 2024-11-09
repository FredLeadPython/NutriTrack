from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.config import Base

class DailyGoal(Base):
    __tablename__ = "daily_goals"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Clé étrangère vers User
    target_calories = Column(Float, nullable=False)
    target_proteins = Column(Float, nullable=False)
    target_carbohydrates = Column(Float, nullable=False)
    target_fats = Column(Float, nullable=False)

    # Relation avec User
    user = relationship("User", back_populates="daily_goals")  # Relation vers User (à définir dans User)

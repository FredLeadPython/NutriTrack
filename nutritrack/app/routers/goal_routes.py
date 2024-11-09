from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from nutritrack.app.config import get_db
from nutritrack.app.models.daily_goal import DailyGoal

router = APIRouter()

class GoalUpdate(BaseModel):
    target_calories: float
    target_proteins: float
    target_carbohydrates: float
    target_fats: float

@router.get("/goals")
def get_goals(user_id: int, db: Session = Depends(get_db)):
    goal = db.query(DailyGoal).filter(DailyGoal.user_id == user_id).first()
    if not goal:
        raise HTTPException(status_code=404, detail="Goals not found")
    return goal

@router.put("/goals")
def update_goals(user_id: int, goals: GoalUpdate, db: Session = Depends(get_db)):
    goal = db.query(DailyGoal).filter(DailyGoal.user_id == user_id).first()
    if not goal:
        raise HTTPException(status_code=404, detail="Goals not found")
    goal.target_calories = goals.target_calories
    goal.target_proteins = goals.target_proteins
    goal.target_carbohydrates = goals.target_carbohydrates
    goal.target_fats = goals.target_fats
    db.commit()
    return {"message": "Goals updated successfully"}

@router.get("/progress")
def get_progress():
    # Calculer les statistiques de l'utilisateur sur une période donnée
    pass  # À implémenter selon la logique métier

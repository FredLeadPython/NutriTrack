from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import Session
from nutritrack.app.config import get_db
from nutritrack.app.models.meal import Meal

router = APIRouter()

class MealCreate(BaseModel):
    date: date
    total_calories: float
    total_proteins: float
    total_carbohydrates: float
    total_fats: float

@router.post("/meals", status_code=status.HTTP_201_CREATED)
def create_meal(meal: MealCreate, db: Session = Depends(get_db)):
    new_meal = Meal(**meal.dict())
    db.add(new_meal)
    db.commit()
    db.refresh(new_meal)
    return new_meal

@router.get("/meals/{date}")
def get_meals_by_date(date: date, db: Session = Depends(get_db)):
    meals = db.query(Meal).filter(Meal.date == date).all()
    return meals

@router.delete("/meals/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_meal(id: int, db: Session = Depends(get_db)):
    meal = db.query(Meal).filter(Meal.id == id).first()
    if not meal:
        raise HTTPException(status_code=404, detail="Meal not found")
    db.delete(meal)
    db.commit()
    return {"message": "Meal deleted"}

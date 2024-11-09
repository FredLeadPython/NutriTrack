from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.config import get_db
from app.models.food import Food

router = APIRouter()

class FoodCreate(BaseModel):
    name: str
    calories: int
    proteins: float
    carbohydrates: float
    fats: float

@router.get("/foods")
def get_foods(db: Session = Depends(get_db)):
    return db.query(Food).all()

@router.post("/foods")
def create_food(food: FoodCreate, db: Session = Depends(get_db)):
    existing_food = db.query(Food).filter_by(name=food.name).first()
    if existing_food is not None:
        raise HTTPException(status_code=400, detail=f"{food.name} item already exists with this name.")

    new_food = Food(**food.model_dump())
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    return new_food
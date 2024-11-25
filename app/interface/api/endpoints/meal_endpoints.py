from application.use_cases.meals.create_meal import create_meal as meal_create
from application.use_cases.meals.get_all_meals import get_all_meals
from fastapi import APIRouter, Depends
from infrastructure.database.db_connection import get_db
from infrastructure.repositories.meal_repository_impl import MealRepositoryImpl
from schemas.meal_schemas import MealCreate, MealResponse
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/meals", response_model=MealResponse)
def create_meal(meal_data: MealCreate, db: Session = Depends(get_db)):
    repository = MealRepositoryImpl(db)
    meal_response: MealResponse = meal_create(
        meal_repository=repository, meal=meal_data
    )
    return meal_response


@router.get("/", response_model=list[MealResponse])
def list_meals(db: Session = Depends(get_db)):
    repository = MealRepositoryImpl(db)
    return get_all_meals(repository=repository)

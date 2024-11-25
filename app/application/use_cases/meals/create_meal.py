from domain.repositories.meal_repository import MealRepository
from infrastructure.database.models.meal_model import MealModel
from schemas.meal_schemas import MealCreate, MealResponse


def create_meal(meal_repository: MealRepository, meal: MealCreate) -> MealResponse:
    meal_model: MealModel = meal_repository.create_meal(meal)
    meal_response = MealResponse(**meal_model.__dict__)
    return meal_response

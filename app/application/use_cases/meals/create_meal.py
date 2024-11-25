from domain.repositories.repository import Repository
from schemas.meal_schemas import MealCreate, MealResponse


def create_meal(meal_repository: Repository, meal: MealCreate) -> MealResponse:
    meal_model = meal_repository.create(meal)
    meal_response = MealResponse(**meal_model.__dict__)
    return meal_response

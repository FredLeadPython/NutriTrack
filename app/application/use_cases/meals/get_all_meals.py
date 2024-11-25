from domain.repositories.meal_repository import MealRepository
from infrastructure.database.models.meal_model import MealModel
from schemas.meal_schemas import MealResponse


def get_all_meals(repository: MealRepository) -> list[MealResponse]:
    meal_models: MealModel = repository.list_meals()
    meal_response = [MealResponse(**meal.__dict__) for meal in meal_models]
    return meal_response

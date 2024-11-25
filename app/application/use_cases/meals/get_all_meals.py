from domain.repositories.repository import Repository
from infrastructure.database.models.meal_model import MealModel
from schemas.meal_schemas import MealResponse


def get_all_meals(repository: Repository) -> list[MealResponse]:
    meal_models: MealModel = repository.get_all()
    meal_response = [MealResponse(**meal.__dict__) for meal in meal_models]
    return meal_response

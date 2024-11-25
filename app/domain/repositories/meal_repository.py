from abc import ABC, abstractmethod
from typing import List, Optional

from infrastructure.database.models.meal_model import MealModel
from schemas.meal_schemas import MealCreate


class MealRepository(ABC):
    @abstractmethod
    def get_meal_by_id(self, meal_id: str) -> Optional[MealModel]:
        pass

    @abstractmethod
    def create_meal(self, meal: MealCreate) -> MealModel:
        pass

    @abstractmethod
    def list_meals(self) -> List[MealModel]:
        pass

from typing import Optional

from schemas.meal_schemas import MealResponse


class Meal:
    def __init__(
        self,
        type: str,
        dietary_preferences: Optional[str],
        allergens: Optional[str],
    ):
        self.type = type
        self.dietary_preferences = dietary_preferences
        self.allergens = allergens

    @classmethod
    def from_meal_result(meal_result: MealResponse):
        return Meal(
            type=meal_result.type,
            dietary_preferences=meal_result.dietary_preferences,
            allergens=meal_result.allergens,
        )

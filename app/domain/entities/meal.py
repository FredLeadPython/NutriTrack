from typing import Optional
from uuid import UUID, uuid4


class Meal:
    def __init__(
        self,
        type: str,
        dietary_preferences: Optional[str],
        allergens: Optional[str],
    ):
        self.id: UUID = uuid4()
        self.type = type
        self.dietary_preferences = dietary_preferences
        self.allergens = allergens

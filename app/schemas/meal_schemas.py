from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class MealBase(BaseModel):
    type: str = Field(..., description="Type of the meal (e.g., Breakfast, Lunch)")
    dietary_preferences: Optional[str] = Field(None, description="Dietary preferences")
    allergens: Optional[str] = Field(None, description="Allergens information")


class MealCreate(MealBase):
    pass  # Same as MealBase for creation


class MealResponse(MealBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)

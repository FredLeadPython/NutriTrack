import uuid
from typing import List, Optional

from domain.entities.meal import Meal
from domain.repositories.meal_repository import MealRepository
from infrastructure.database.models.meal_model import MealModel
from sqlalchemy.orm import Session


class MealRepositoryImpl(MealRepository):
    def __init__(self, db_session: Session):
        """
        Initialise le repository avec une session de base de données.
        :param db_session: La session SQLAlchemy utilisée pour les transactions.
        """
        self.db_session = db_session

    def get_meal_by_id(self, meal_id: str) -> Optional[MealModel]:
        """
        Récupère un repas par son ID.
        :param meal_id: L'identifiant du repas.
        :return: Une instance de Meal ou None si non trouvé.
        """
        meal_model = (
            self.db_session.query(MealModel).filter(MealModel.id == meal_id).first()
        )
        if meal_model:
            return MealModel(
                id=meal_model.id,
                type=meal_model.type,
                dietary_preferences=meal_model.dietary_preferences,
                allergens=meal_model.allergens,
            )
        return None

    def create_meal(self, meal: Meal) -> MealModel:
        meal_model = MealModel(id=str(uuid.uuid4()), **meal.__dict__)
        self.db_session.add(meal_model)
        self.db_session.commit()
        self.db_session.refresh(meal_model)
        return meal_model

    def list_meals(self) -> List[MealModel]:
        """
        Récupère la liste de tous les repas.
        :return: Une liste d'instances de Meal.
        """
        meal_models = self.db_session.query(MealModel).all()
        return meal_models

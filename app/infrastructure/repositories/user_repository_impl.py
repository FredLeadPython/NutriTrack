from typing import List, Optional
from uuid import uuid4

from domain.entities.user import User
from domain.repositories.user_repository import UserRepository
from infrastructure.database.models.user_model import UserModel
from schemas.user_schemas import UserCreate, UserResult
from sqlalchemy.orm import Session


class UserRepositoryImpl(UserRepository):
    def __init__(self, db_session: Session):
        """
        Initialise le repository avec une session de base de données.
        :param db_session: La session SQLAlchemy utilisée pour les transactions.
        """
        self.db_session = db_session

    def get_user_by_id(self, user_id: str) -> Optional[UserResult]:
        """
        Récupère un utilisateur par son ID.
        :param user_id: L'identifiant de l'utilisateur.
        :return: Une instance de User ou None si non trouvé.
        """
        user_model = (
            self.db_session.query(UserModel).filter(UserModel.id == user_id).first()
        )
        if user_model:
            return User(
                username=user_model.username, email=user_model.email, age=user_model.age
            )
        return None

    def create_user(self, user: UserCreate) -> UserResult:
        """
        Crée un nouvel utilisateur en base de données.
        :param user: Une instance de User.
        :return: L'utilisateur créé.
        """
        user_model = (
            self.db_session.query(UserModel)
            .filter(UserModel.email == user.email)
            .first()
        )
        if user_model:
            return None

        user_model = UserModel(id=str(uuid4()), **user.__dict__)

        self.db_session.add(user_model)
        self.db_session.commit()
        self.db_session.refresh(user_model)

        return UserResult(**user_model.__dict__)

    def list_users(self) -> List[UserResult]:
        """
        Récupère la liste de tous les utilisateurs.
        :return: Une liste d'instances de User.
        """
        user_models = self.db_session.query(UserModel).all()
        return [UserResult(**user_model.__dict__) for user_model in user_models]

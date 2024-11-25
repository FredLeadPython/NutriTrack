from typing import List, Optional
from uuid import uuid4

from domain.repositories.repository import Repository
from infrastructure.database.models.user_model import UserModel
from schemas.user_schemas import UserCreate, UserResult
from sqlalchemy.orm import Session


class UserRepositoryImpl(Repository):
    def __init__(self, db_session: Session):
        """
        Initialise le repository avec une session de base de données.
        :param db_session: La session SQLAlchemy utilisée pour les transactions.
        """
        self.db_session = db_session

    def get_by_id(self, id: str) -> Optional[UserResult]:
        """
        Récupère un utilisateur par son ID.
        :param user_id: L'identifiant de l'utilisateur.
        :return: Une instance de User ou None si non trouvé.
        """
        user_model = self.db_session.query(UserModel).filter(UserModel.id == id).first()
        if user_model:
            return UserResult(**user_model.__dict__)
        return None

    def get_by_email(self, email: str) -> UserModel:
        user_model = (
            self.db_session.query(UserModel).filter(UserModel.email == email).first()
        )

        return user_model

    def create(self, user: UserCreate) -> None:
        """
        Crée un nouvel utilisateur en base de données.
        :param user: Une instance de User.
        :return: L'utilisateur créé.
        """
        user_model = self.get_by_email(email=user.email)
        if user_model:
            return None

        user_model = UserModel(id=str(uuid4()), **user.__dict__)

        self.db_session.add(user_model)
        self.db_session.commit()
        self.db_session.refresh(user_model)

        return UserResult(**user_model.__dict__)

    def get_all(self) -> List[UserResult]:
        """
        Récupère la liste de tous les utilisateurs.
        :return: Une liste d'instances de User.
        """
        user_models = self.db_session.query(UserModel).all()
        return [UserResult(**user_model.__dict__) for user_model in user_models]

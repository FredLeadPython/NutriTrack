from domain.repositories.repository import Repository
from schemas.user_schemas import UserCreate, UserResult


def create_user(repository: Repository, user: UserCreate) -> UserResult:
    repository.create(user)

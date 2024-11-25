from domain.repositories.user_repository import UserRepository
from schemas.user_schemas import UserCreate, UserResult


def create_user(repository: UserRepository, user: UserCreate) -> UserResult:
    return repository.create_user(user)

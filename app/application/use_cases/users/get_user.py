from domain.repositories.user_repository import UserRepository
from schemas.user_schemas import UserResult


def get_user(repository: UserRepository, user_id: str) -> UserResult:
    return repository.get_user_by_id(user_id=user_id)

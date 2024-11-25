from domain.repositories.repository import Repository
from schemas.user_schemas import UserResult


def get_user(repository: Repository, user_id: str) -> UserResult:
    return repository.get_by_id(id=user_id)

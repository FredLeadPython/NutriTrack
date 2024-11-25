from domain.repositories.user_repository import UserRepository
from schemas.user_schemas import UserResult


def get_list_users(repository: UserRepository) -> list[UserResult]:
    return repository.list_users()

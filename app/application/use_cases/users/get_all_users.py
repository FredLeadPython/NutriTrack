from domain.repositories.repository import Repository
from schemas.user_schemas import UserResult


def get_list_users(repository: Repository) -> list[UserResult]:
    return repository.get_all()

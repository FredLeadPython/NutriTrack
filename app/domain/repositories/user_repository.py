from abc import ABC, abstractmethod
from typing import List, Optional

from schemas.user_schemas import UserCreate, UserResult


class UserRepository(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: str) -> Optional[UserResult]:
        pass

    @abstractmethod
    def create_user(self, user: UserCreate) -> UserResult:
        pass

    @abstractmethod
    def list_users(self) -> List[UserResult]:
        pass

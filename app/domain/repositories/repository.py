from abc import ABC, abstractmethod
from typing import Optional

from pydantic import BaseModel


class Repository(ABC):
    def __init__(self, db):
        self.db = db

    @abstractmethod
    def get_by_id(self, id: str) -> Optional[BaseModel]:
        pass

    @abstractmethod
    def create(self, model: BaseModel) -> None:
        pass

    @abstractmethod
    def get_all(self) -> list[BaseModel]:
        pass

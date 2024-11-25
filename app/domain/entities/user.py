from typing import Optional
from uuid import UUID, uuid4


class User:
    def __init__(self, username: str, email: str, age: Optional[int] = None):
        self.id: UUID = uuid4()
        self.username = username
        self.email = email
        self.age = age

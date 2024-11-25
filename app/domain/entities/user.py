from typing import Optional

from schemas.user_schemas import UserResult


class User:
    def __init__(self, username: str, email: str, age: Optional[int] = None):
        self.username = username
        self.email = email
        self.age = age

    @classmethod
    def from_user_result(user_result: UserResult):
        return User(
            username=user_result.username, email=user_result.email, age=user_result.age
        )

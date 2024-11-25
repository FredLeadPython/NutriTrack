from application.use_cases.users.create_user import create_user as user_create
from application.use_cases.users.get_all_users import get_list_users as users_get_list
from application.use_cases.users.get_user import get_user
from fastapi import APIRouter, Depends
from infrastructure.database.db_connection import get_db
from infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from schemas.user_schemas import UserCreate, UserResult
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/user", response_model=None)
def create_user(user: UserCreate, db: Session = Depends(get_db)) -> UserResult:
    user_repo = UserRepositoryImpl(db)
    user_result = user_create(repository=user_repo, user=user)
    return user_result


@router.get("/")
def get_list_users(db: Session = Depends(get_db)) -> list[UserResult]:
    user_repo = UserRepositoryImpl(db)
    users = users_get_list(repository=user_repo)
    return users


@router.get("/user/{user_id}", response_model=None)
def get_user_by_id(user_id: str, db: Session = Depends(get_db)) -> UserResult:
    user_repo = UserRepositoryImpl(db)
    user = get_user(repository=user_repo, user_id=user_id)
    return user

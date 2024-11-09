from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.config import get_db
from app.models.user import User
from typing import Optional

router = APIRouter()

# Schémas de données pour les requêtes
class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserPreferences(BaseModel):
    preferences: Optional[str]


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: UserRegister, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = User(username=user.username, email=user.email, hashed_password=user.password)  # Hasher le mot de passe en production
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}

@router.post("/login")
def login():
    # Authentification et génération de token (JWT)
    pass  # À implémenter avec JWT

@router.get("/user/preferences")
def get_preferences(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"preferences": user.preferences}

@router.put("/user/preferences")
def update_preferences(user_id: int, preferences: UserPreferences, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.preferences = preferences.preferences
    db.commit()
    return {"message": "Preferences updated successfully"}

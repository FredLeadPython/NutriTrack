from fastapi import FastAPI
from infrastructure.database.db_connection import engine
from infrastructure.database.models.association_table import (  # Charger l'association
    user_meal_association,
)
from infrastructure.database.models.base import Base
from infrastructure.database.models.meal_model import MealModel  # Charger les modèles
from infrastructure.database.models.user_model import UserModel  # Charger les modèles
from interface.api.endpoints.meal_endpoints import router as meal_endpoint_router
from interface.api.endpoints.user_endpoints import router as user_endpoint_router


# Création des tables (important pour SQLite)
Base.metadata.create_all(bind=engine)

# Initialisation de l'application FastAPI
app = FastAPI(
    title="NutriTrack API",
    description="API for NutriTrack, a nutrition tracking application.",
    version="1.0.0",
)

# Inclusion des routes (endpoints)
app.include_router(user_endpoint_router, prefix="/users", tags=["Users"])
app.include_router(meal_endpoint_router, prefix="/meals", tags=["Meals"])


# Endpoint de base pour vérifier si l'application tourne
@app.get("/")
def read_root():
    return {"message": "Welcome to NutriTrack API"}

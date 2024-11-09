from fastapi import FastAPI
from app.routers import user_routes, meal_routes, food_routes, goal_routes

app = FastAPI()

# Enregistrement des routes
app.include_router(user_routes.router)
app.include_router(meal_routes.router)
app.include_router(food_routes.router)
app.include_router(goal_routes.router)

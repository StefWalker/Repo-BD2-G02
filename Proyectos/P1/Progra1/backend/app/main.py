from fastapi import FastAPI
from .routes import survey_routes, auth_routes, user_routes  # Crear estas rutas

app = FastAPI()

# Incluir rutas
app.include_router(survey_routes.router, prefix="/surveys")
app.include_router(auth_routes.router, prefix="/auth")
app.include_router(user_routes.router, prefix="/users")

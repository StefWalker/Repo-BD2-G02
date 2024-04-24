from fastapi import APIRouter

router = APIRouter()

# Listar todos los usuarios
@router.get("/")
async def list_users():
    # Implementar lógica para obtener la lista de usuarios
    return [{"username": "usuario1"}, {"username": "usuario2"}]

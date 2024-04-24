from fastapi import APIRouter

router = APIRouter()

# Ruta para listar todas las encuestas (por ejemplo)
@router.get("/")
async def list_surveys():
    return {"message": "Aquí se listarán las encuestas"}

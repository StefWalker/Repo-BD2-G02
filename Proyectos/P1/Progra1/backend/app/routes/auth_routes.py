from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import User
from pydantic import BaseModel
import bcrypt  # Para manejar contraseñas seguras

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo para crear un usuario
class UserCreate(BaseModel):
    username: str
    password: str

@router.post("/register")
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Verificar si el usuario ya existe
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")

    # Hash de la contraseña antes de guardarla
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

    # Crear un nuevo usuario
    new_user = User(username=user.username, password=hashed_password)

    # Guardar el usuario en la base de datos
    db.add(new_user)
    db.commit()

    return {"message": "Usuario registrado con éxito"}

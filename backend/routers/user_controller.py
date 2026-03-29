# Librerias
#from http.client import HTTPException
#from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
#from utils.functions import hash_password
# Importar directorios del proyecto
from services import (
    get_all_users as get_all_service, \
    search_users_by_id_or_email as search_by_id_or_email_service, \
    search_user_by_id as search_by_id_service, \
    create_user_service)
from schemas import UserCreate, UserResponse
from database import get_db


# Instancia del router de usuarios
user_controller = APIRouter()


# RUTAS DE USUARIOS
@user_controller.get("/users", tags=["users"],
                     description="Endpoint para obtener todos los usuarios del sistema")
async def get_users(db: Session = Depends(get_db)) -> dict[str, object]:
    users_list = get_all_service(db)
    return {"message": "List of users", "users": users_list}

@user_controller.get("/users/{user_id}", tags=["users"],
                     description="Endpoint para obtener un usuario específico por su ID")
async def get_user(db: Session = Depends(get_db), user_id: str | None = None) -> dict[str, object]:
    user = search_by_id_service(db, user_id)
    # Si no encuentra el usuario, devolver un mensaje de error
    if not user:
        return {"message": "User not found"}
    return {"message": "User found", "user": user}

@user_controller.post("/users/create", tags=["users"],
                      description="Endpoint para obtener un usuario específico por su ID o correo electrónico")
async def get_user_by_id_or_email(db: Session = Depends(get_db), id: str | None = None,
                                  email: str | None = None) -> dict[str, object]:
    user = search_by_id_or_email_service(db, id, email)
    # Si no encuentra el usuario, devolver un mensaje de error
    if not user:
        return {"message": "User not found"}
    return {"message": "User found", "user": user}

""" @user_controller.post("/users/create")
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> dict[str, object]:
    new_user: dict[str, object] = {
        "id": user.id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "password": hash_password(user.password),
        "email": user.email,
        "role_id": user.role_id,
        "is_active": True
        }
    
    try:
        create_user_service(user, db)
    except Exception as e:
        return {"message": "Error creating user", "error": str(e)}
    
    return {"message": "User created", "user": new_user} """

@user_controller.post("/users/create", tags=["users"],
                      description="Endpoint para crear un nuevo usuario en el sistema")
async def create_user(
    user: UserCreate, db: Session = Depends(get_db)
    ) -> dict[str, UserResponse] | dict[str, object]:
    
    try:
        created_user = create_user_service(user, db)
        if not created_user:
            return {"message": "Error creating user", "user": None}
        
        user_response = UserResponse.model_validate(created_user)
        return {"message": "User created", "user": user_response}
    
    except Exception as e:
        return {"message": "Error creating user", "error": str(e)}
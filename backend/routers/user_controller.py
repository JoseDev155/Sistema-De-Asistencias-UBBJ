# Librerias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from services import (
    create_user_service,
    delete_user_service,
    destroy_user_service,
    get_all_users as get_all_service,
    search_users_by_id_or_email as search_by_id_or_email_service,
    search_user_by_id as search_by_id_service,
    search_user_by_name as search_by_name_service,
    update_user_service,
    reactivate_user_service
)
from schemas import UserCreate, UserResponse, UserUpdate
from database import get_db
from models import User
from utils import get_current_admin_user


# Instancia del router de usuarios
user_controller = APIRouter()


# RUTAS DE USUARIOS - SOLO ADMIN
@user_controller.get("/users", tags=["users"],
                     description="Endpoint para obtener todos los usuarios del sistema. Solo Admin.")
async def get_users(
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    users_list = get_all_service(db)
    return {"message": "List of users", "users": users_list}


@user_controller.get("/users/{user_id}", tags=["users"],
                     description="Endpoint para obtener un usuario específico por su ID. Solo Admin.")
async def get_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    user = search_by_id_service(db, user_id)
    if not user:
        return {"message": "User not found"}
    return {"message": "User found", "user": user}


@user_controller.post("/users/search", tags=["users"],
                      description="Endpoint para buscar un usuario por ID o email. Solo Admin.")
async def search_user_by_id_or_email(
    db: Session = Depends(get_db),
    id: str | None = None,
    email: str | None = None,
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    user = search_by_id_or_email_service(db, id, email)
    if not user:
        return {"message": "User not found"}
    return {"message": "User found", "user": user}


@user_controller.get("/users/search/name/{user_name}", tags=["users"],
                     description="Endpoint para obtener un usuario por su nombre. Solo Admin.")
async def get_user_by_name(
    user_name: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    user = search_by_name_service(db, user_name)
    if not user:
        return {"message": "User not found"}
    return {"message": "User found", "user": user}


@user_controller.post("/users", tags=["users"],
                      description="Endpoint para crear un nuevo usuario en el sistema. Solo Admin.")
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, UserResponse] | dict[str, object]:
    try:
        created_user = create_user_service(user, db)
        if not created_user:
            return {"message": "Error creating user", "user": None}
        
        user_response = UserResponse.model_validate(created_user)
        return {"message": "User created", "user": user_response}
    except Exception as e:
        return {"message": "Error creating user", "error": str(e)}


@user_controller.put("/users/{user_id}", tags=["users"],
                     description="Endpoint para actualizar un usuario específico por su ID. Solo Admin.",
                     response_model=UserResponse)
async def update_user(
    user_id: str,
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, UserResponse] | dict[str, object]:
    try:
        updated_user = update_user_service(user_id, user, db)
        if not updated_user:
            return {"message": "Usuario no encontrado o no pudo ser actualizado", "user": None}
        
        user_response = UserResponse.model_validate(updated_user)
        return {"message": "Usuario actualizado", "user": user_response}
    except Exception as e:
        return {"message": "Error al actualizar el usuario", "error": str(e)}


@user_controller.delete("/users/{user_id}", tags=["users"],
                        description="Endpoint para eliminar (soft delete) un usuario específico por su ID. Solo Admin.")
async def delete_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    success = delete_user_service(user_id, db)
    if success:
        return {"message": "Usuario eliminado exitosamente"}
    else:
        return {"message": "Usuario no encontrado o no pudo ser eliminado"}


@user_controller.post("/users/{user_id}/reactivate", tags=["users"],
                      description="Endpoint para reactivar un usuario específico por su ID. Solo Admin.",
                      response_model=UserResponse)
async def reactivate_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    try:
        user = reactivate_user_service(user_id, db)
        if not user:
            return {"message": "Usuario no encontrado o no pudo ser reactivado", "user": None}
        
        user_response = UserResponse.model_validate(user)
        return {"message": "Usuario reactivado", "user": user_response}
    except Exception as e:
        return {"message": "Error al reactivar el usuario", "error": str(e)}


@user_controller.delete("/users/{user_id}/destroy", tags=["users"],
                        description="Endpoint para eliminar definitivamente un usuario específico por su ID. Solo Admin.")
async def destroy_user(
    user_id: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    try:
        success = destroy_user_service(user_id, db)
        if success:
            return {"message": "Usuario eliminado definitivamente"}
        else:
            return {"message": "Usuario no encontrado o no pudo ser eliminado definitivamente"}
    except Exception as e:
        return {"message": "Error al eliminar definitivamente el usuario", "error": str(e)}
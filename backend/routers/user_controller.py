# Librerias
#from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from services import (
    create_user_service, \
    delete_user_service, \
    destroy_user_service, \
    get_all_users as get_all_service, \
    search_users_by_id_or_email as search_by_id_or_email_service, \
    search_user_by_id as search_by_id_service, \
    search_user_by_name as search_by_name_service, \
    update_user_service, \
    reactivate_user_service)
from schemas import UserCreate, UserResponse, UserUpdate
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

@user_controller.get("/users/{user_id}", tags=["users"],
                     description="Endpoint para obtener un usuario específico por su ID")
async def get_user_by_name(db: Session = Depends(get_db), user_name: str | None = None) -> dict[str, object]:
    # Busca el usuario por su "first_name"
    user = search_by_name_service(db, user_name)
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

@user_controller.put("/users/{id}", tags=["users"],
                     description="Endpoint para actualizar un usuario específico por su ID",
                     response_model=UserResponse)
async def update_user(
    id: str, user: UserUpdate, db: Session = Depends(get_db)
    ) -> dict[str, UserResponse] | dict[str, object]:
    # Bloque de validacion
    try:
        updated_user = update_user_service(id, user, db)
        if not updated_user:
            return {"message": "Usuario no encontrado o no pudo ser actualizado", "user": None}
        
        user_response = UserResponse.model_validate(updated_user)
        return {"message": "Usuario actualizado", "user": user_response}
    except Exception as e:
        return {"message": "Error al actualizar el usuario", "error": str(e)}

@user_controller.delete("/users/{id}", tags=["users"],
                        description="Endpoint para eliminar un usuario específico por su ID")
async def delete_user(id: str, db: Session = Depends(get_db)) -> dict[str, object]:
    # Borrado logico, no definitivo
    success = delete_user_service(id, db)
    if success:
        return {"message": "Usuario eliminado exitosamente"}
    else:
        return {"message": "Usuario no encontrado o no pudo ser eliminado"}

@user_controller.post("/users/{id}/reactivate", tags=["users"],
                        description="Endpoint para reactivar un usuario específico por su ID",
                        response_model=UserResponse)
async def reactivate_user(id: str, db: Session = Depends(get_db)) -> dict[str, object]:
    try:
        user = reactivate_user_service(id, db)
        if not user:
            return {"message": "Usuario no encontrado o no pudo ser reactivado", "user": None}
        
        user_response = UserResponse.model_validate(user)
        return {"message": "Usuario reactivado", "user": user_response}
    except Exception as e:
        return {"message": "Error al reactivar el usuario", "error": str(e)}

@user_controller.delete("/users/{id}/destroy", tags=["users"],
                        description="Endpoint para eliminar definitivamente un usuario específico por su ID")
async def destroy_user(id: str, db: Session = Depends(get_db)) -> dict[str, object]:
    try:
        # Borrado definitivo
        success = destroy_user_service(id, db)
        if success:
            return {"message": "Usuario eliminado definitivamente"}
        else:
            return {"message": "Usuario no encontrado o no pudo ser eliminado definitivamente"}
    except Exception as e:
        return {"message": "Error al eliminar definitivamente el usuario", "error": str(e)}
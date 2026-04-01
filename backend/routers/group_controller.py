# Librerias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from services import (
    create_group_service,
    destroy_group_service,
    get_all_groups as get_all_service,
    search_group_by_id as search_by_id_service,
    search_groups_by_name as search_by_name_service,
    update_group_service
)
from schemas import GroupCreate, GroupResponse, GroupUpdate
from database import get_db
from models import User
from utils import get_current_admin_user, get_current_professor_or_admin_user


# Instancia del router de grupos
group_controller = APIRouter()


# RUTAS DE GRUPOS - SOLO ADMIN
@group_controller.get("/groups", tags=["groups"],
                     description="Endpoint para obtener todos los grupos del sistema. Admin y Profesor.",
                     response_model=list[GroupResponse])
async def get_groups(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    groups_list = get_all_service(db)
    return {"message": "Lista de grupos", "groups": groups_list}

@group_controller.get("/groups/{id}", tags=["groups"],
                     description="Endpoint para obtener un grupo específico por su ID. Admin y Profesor.",
                     response_model=GroupResponse)
async def get_group(
    id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    group = search_by_id_service(db, id)
    if not group:
        return {"message": "Grupo no encontrado"}
    return {"message": "Grupo encontrado", "group": group}

@group_controller.get("/groups/search/{name}", tags=["groups"],
                     description="Endpoint para obtener un grupo específico por su nombre. Admin y Profesor.",
                     response_model=GroupResponse)
async def get_group_by_name(
    name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    group = search_by_name_service(db, name)
    if not group:
        return {"message": "Grupo no encontrado"}
    return {"message": "Grupo encontrado", "group": group}

@group_controller.post("/groups", tags=["groups"],
                      description="Endpoint para crear un nuevo grupo en el sistema. Solo Admin.",
                      response_model=GroupResponse)
async def create_group(
    group: GroupCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, GroupResponse] | dict[str, object]:
    try:
        created_group = create_group_service(group, db)
        if not created_group:
            return {"message": "Error al crear el grupo", "group": None}
        
        group_response = GroupResponse.model_validate(created_group)
        return {"message": "Grupo creado", "group": group_response}
    except Exception as e:
        return {"message": "Error al crear el grupo", "error": str(e)}

@group_controller.put("/groups/{id}", tags=["groups"],
                     description="Endpoint para actualizar un grupo específico por su ID. Solo Admin.",
                     response_model=GroupResponse)
async def update_group(
    id: str,
    group: GroupUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, GroupResponse] | dict[str, object]:
    try:
        updated_group = update_group_service(id, group, db)
        if not updated_group:
            return {"message": "Grupo no encontrado o no pudo ser actualizado", "group": None}
        
        group_response = GroupResponse.model_validate(updated_group)
        return {"message": "Grupo actualizado", "group": group_response}
    except Exception as e:
        return {"message": "Error al actualizar el grupo", "error": str(e)}

@group_controller.delete("/groups/{id}", tags=["groups"],
                        description="Endpoint para eliminar un grupo específico por su ID. Solo Admin.")
async def delete_group(
    id: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    success = destroy_group_service(id, db)
    if success:
        return {"message": "Grupo eliminado exitosamente"}
    else:
        return {"message": "Grupo no encontrado o no pudo ser eliminado"}

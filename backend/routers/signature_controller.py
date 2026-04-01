# Librerias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from services import (
    create_signature_service,
    destroy_signature_service,
    get_all_signatures as get_all_service,
    search_signature_by_id as search_by_id_service,
    search_signatures_by_name as search_by_name_service,
    update_signature_service
)
from schemas import SignatureCreate, SignatureResponse, SignatureUpdate
from database import get_db
from models import User
from utils import get_current_admin_user, get_current_professor_or_admin_user


# Instancia del router de asignaturas
signature_controller = APIRouter()


# RUTAS DE ASIGNATURAS - SOLO ADMIN
@signature_controller.get("/signatures", tags=["signatures"],
                         description="Endpoint para obtener todas las asignaturas del sistema. Admin y Profesor.",
                         response_model=list[SignatureResponse])
async def get_signatures(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    signatures_list = get_all_service(db)
    return {"message": "Lista de asignaturas", "signatures": signatures_list}

@signature_controller.get("/signatures/{id}", tags=["signatures"],
                         description="Endpoint para obtener una asignatura específica por su ID. Admin y Profesor.",
                         response_model=SignatureResponse)
async def get_signature(
    id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    signature = search_by_id_service(db, id)
    if not signature:
        return {"message": "Asignatura no encontrada"}
    return {"message": "Asignatura encontrada", "signature": signature}

@signature_controller.get("/signatures/search/{name}", tags=["signatures"],
                         description="Endpoint para obtener una asignatura específica por su nombre. Admin y Profesor.",
                         response_model=SignatureResponse)
async def get_signature_by_name(
    name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    signature = search_by_name_service(db, name)
    if not signature:
        return {"message": "Asignatura no encontrada"}
    return {"message": "Asignatura encontrada", "signature": signature}

@signature_controller.post("/signatures", tags=["signatures"],
                          description="Endpoint para crear una nueva asignatura en el sistema. Solo Admin.",
                          response_model=SignatureResponse)
async def create_signature(
    signature: SignatureCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, SignatureResponse] | dict[str, object]:
    try:
        created_signature = create_signature_service(signature, db)
        if not created_signature:
            return {"message": "Error al crear la asignatura", "signature": None}
        
        signature_response = SignatureResponse.model_validate(created_signature)
        return {"message": "Asignatura creada", "signature": signature_response}
    except Exception as e:
        return {"message": "Error al crear la asignatura", "error": str(e)}

@signature_controller.put("/signatures/{id}", tags=["signatures"],
                         description="Endpoint para actualizar una asignatura específica por su ID. Solo Admin.",
                         response_model=SignatureResponse)
async def update_signature(
    id: str,
    signature: SignatureUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, SignatureResponse] | dict[str, object]:
    try:
        updated_signature = update_signature_service(id, signature, db)
        if not updated_signature:
            return {"message": "Asignatura no encontrada o no pudo ser actualizada", "signature": None}
        
        signature_response = SignatureResponse.model_validate(updated_signature)
        return {"message": "Asignatura actualizada", "signature": signature_response}
    except Exception as e:
        return {"message": "Error al actualizar la asignatura", "error": str(e)}

@signature_controller.delete("/signatures/{id}", tags=["signatures"],
                            description="Endpoint para eliminar una asignatura específica por su ID. Solo Admin.")
async def delete_signature(
    id: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    success = destroy_signature_service(id, db)
    if success:
        return {"message": "Asignatura eliminada exitosamente"}
    else:
        return {"message": "Asignatura no encontrada o no pudo ser eliminada"}

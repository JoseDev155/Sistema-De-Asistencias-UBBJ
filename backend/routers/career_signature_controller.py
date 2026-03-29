# Librerias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from services import (
    create_career_signature_service, \
    destroy_career_signature_service, \
    get_all_career_signatures as get_all_service, \
    search_career_signature_by_id as search_by_id_service, \
    update_career_signature_service)
from schemas import CareerSignatureCreate, CareerSignatureResponse, CareerSignatureUpdate
from database import get_db


# Instancia del router de carrera-asignatura
career_signature_controller = APIRouter()


# RUTAS DE CARRERA-ASIGNATURA
@career_signature_controller.get("/career-signatures", tags=["career-signatures"],
                                 description="Endpoint para obtener todas las carrera-asignatura del sistema",
                                 response_model=list[CareerSignatureResponse])
async def get_career_signatures(db: Session = Depends(get_db)) -> dict[str, object]:
    career_sigs_list = get_all_service(db)
    return {"message": "Lista de carrera-asignatura", "career_signatures": career_sigs_list}

@career_signature_controller.get("/career-signatures/{id}", tags=["career-signatures"],
                                 description="Endpoint para obtener una carrera-asignatura específica por su ID",
                                 response_model=CareerSignatureResponse)
async def get_career_signature(id: str, db: Session = Depends(get_db)) -> dict[str, object]:
    career_sig = search_by_id_service(db, id)
    if not career_sig:
        return {"message": "Carrera-asignatura no encontrada"}
    return {"message": "Carrera-asignatura encontrada", "career_signature": career_sig}

@career_signature_controller.post("/career-signatures", tags=["career-signatures"],
                                  description="Endpoint para crear una nueva carrera-asignatura en el sistema",
                                  response_model=CareerSignatureResponse)
async def create_career_signature(
    career_sig: CareerSignatureCreate, db: Session = Depends(get_db)
    ) -> dict[str, CareerSignatureResponse] | dict[str, object]:
    try:
        created_career_sig = create_career_signature_service(career_sig, db)
        if not created_career_sig:
            return {"message": "Error al crear la carrera-asignatura", "career_signature": None}
        
        career_sig_response = CareerSignatureResponse.model_validate(created_career_sig)
        return {"message": "Carrera-asignatura creada", "career_signature": career_sig_response}
    except Exception as e:
        return {"message": "Error al crear la carrera-asignatura", "error": str(e)}

@career_signature_controller.put("/career-signatures/{id}", tags=["career-signatures"],
                                 description="Endpoint para actualizar una carrera-asignatura específica por su ID",
                                 response_model=CareerSignatureResponse)
async def update_career_signature(
    id: str, career_sig: CareerSignatureUpdate, db: Session = Depends(get_db)
    ) -> dict[str, CareerSignatureResponse] | dict[str, object]:
    try:
        updated_career_sig = update_career_signature_service(id, career_sig, db)
        if not updated_career_sig:
            return {"message": "Carrera-asignatura no encontrada o no pudo ser actualizada", "career_signature": None}
        
        career_sig_response = CareerSignatureResponse.model_validate(updated_career_sig)
        return {"message": "Carrera-asignatura actualizada", "career_signature": career_sig_response}
    except Exception as e:
        return {"message": "Error al actualizar la carrera-asignatura", "error": str(e)}

@career_signature_controller.delete("/career-signatures/{id}", tags=["career-signatures"],
                                    description="Endpoint para eliminar una carrera-asignatura específica por su ID")
async def delete_career_signature(id: str, db: Session = Depends(get_db)) -> dict[str, object]:
    success = destroy_career_signature_service(id, db)
    if success:
        return {"message": "Carrera-asignatura eliminada exitosamente"}
    else:
        return {"message": "Carrera-asignatura no encontrada o no pudo ser eliminada"}

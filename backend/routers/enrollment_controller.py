# Librerias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import date
# Importar directorios del proyecto
from services import (
    create_enrollment_service, \
    destroy_enrollment_service, \
    get_all_enrollments as get_all_service, \
    search_enrollments_by_date as search_by_date_service, \
    search_enrollment_by_id as search_by_id_service, \
    update_enrollment_service)
from schemas import EnrollmentCreate, EnrollmentResponse, EnrollmentUpdate
from database import get_db


# Instancia del router de inscripciones
enrollment_controller = APIRouter()


# RUTAS DE INSCRIPCIONES
@enrollment_controller.get("/enrollments", tags=["enrollments"],
                           description="Endpoint para obtener todas las inscripciones del sistema",
                           response_model=list[EnrollmentResponse])
async def get_enrollments(db: Session = Depends(get_db)) -> dict[str, object]:
    enrollments_list = get_all_service(db)
    return {"message": "Lista de inscripciones", "enrollments": enrollments_list}

@enrollment_controller.get("/enrollments/{id}", tags=["enrollments"],
                           description="Endpoint para obtener una inscripción específica por su ID",
                           response_model=EnrollmentResponse)
async def get_enrollment(id: int, db: Session = Depends(get_db)) -> dict[str, object]:
    enrollment = search_by_id_service(db, id)
    if not enrollment:
        return {"message": "Inscripción no encontrada"}
    return {"message": "Inscripción encontrada", "enrollment": enrollment}

@enrollment_controller.get("/enrollments/search/{enrollment_date}", tags=["enrollments"],
                           description="Endpoint para obtener una inscripción específica por fecha",
                           response_model=EnrollmentResponse)
async def get_enrollment_by_date(enrollment_date: date, db: Session = Depends(get_db)) -> dict[str, object]:
    enrollment = search_by_date_service(db, enrollment_date)
    if not enrollment:
        return {"message": "Inscripción no encontrada"}
    return {"message": "Inscripción encontrada", "enrollment": enrollment}

@enrollment_controller.post("/enrollments", tags=["enrollments"],
                            description="Endpoint para crear una nueva inscripción en el sistema",
                            response_model=EnrollmentResponse)
async def create_enrollment(
    enrollment: EnrollmentCreate, db: Session = Depends(get_db)
    ) -> dict[str, EnrollmentResponse] | dict[str, object]:
    try:
        created_enrollment = create_enrollment_service(enrollment, db)
        if not created_enrollment:
            return {"message": "Error al crear la inscripción", "enrollment": None}
        
        enrollment_response = EnrollmentResponse.model_validate(created_enrollment)
        return {"message": "Inscripción creada", "enrollment": enrollment_response}
    except Exception as e:
        return {"message": "Error al crear la inscripción", "error": str(e)}

@enrollment_controller.put("/enrollments/{id}", tags=["enrollments"],
                           description="Endpoint para actualizar una inscripción específica por su ID",
                           response_model=EnrollmentResponse)
async def update_enrollment(
    id: int, enrollment: EnrollmentUpdate, db: Session = Depends(get_db)
    ) -> dict[str, EnrollmentResponse] | dict[str, object]:
    try:
        updated_enrollment = update_enrollment_service(id, enrollment, db)
        if not updated_enrollment:
            return {"message": "Inscripción no encontrada o no pudo ser actualizada", "enrollment": None}
        
        enrollment_response = EnrollmentResponse.model_validate(updated_enrollment)
        return {"message": "Inscripción actualizada", "enrollment": enrollment_response}
    except Exception as e:
        return {"message": "Error al actualizar la inscripción", "error": str(e)}

@enrollment_controller.delete("/enrollments/{id}", tags=["enrollments"],
                              description="Endpoint para eliminar una inscripción específica por su ID")
async def delete_enrollment(id: int, db: Session = Depends(get_db)) -> dict[str, object]:
    success = destroy_enrollment_service(id, db)
    if success:
        return {"message": "Inscripción eliminada exitosamente"}
    else:
        return {"message": "Inscripción no encontrada o no pudo ser eliminada"}

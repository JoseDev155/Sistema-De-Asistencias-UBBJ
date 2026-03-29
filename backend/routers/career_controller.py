# Librerias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from services import (
    create_career_service, \
    delete_career_service, \
    destroy_career_service, \
    get_all_careers as get_all_service, \
    reactivate_career_service, \
    search_career_by_id as search_by_id_service, \
    search_careers_by_name as search_by_name_service, \
    update_career_service)
from schemas import CareerCreate, CareerResponse, CareerUpdate
from database import get_db


# Instancia del router de carreras
career_controller = APIRouter()


# RUTAS DE CARRERAS
@career_controller.get("/careers", tags=["careers"],
                     description="Endpoint para obtener todas las carreras del sistema",
                     response_model=list[CareerResponse])
async def get_careers(db: Session = Depends(get_db)) -> dict[str, object]:
    careers_list = get_all_service(db)
    return {"message": "Lista de carreras", "careers": careers_list}

@career_controller.get("/careers/{id}", tags=["careers"],
                     description="Endpoint para obtener una carrera específica por su ID",
                     response_model=CareerResponse)
async def get_career(id: int, db: Session = Depends(get_db)) -> dict[str, object]:
    career = search_by_id_service(db, id)
    # Si no encuentra la carrera, devolver un mensaje de error
    if not career:
        return {"message": "Carrera no encontrada"}
    return {"message": "Carrera encontrada", "career": career}

@career_controller.get("/careers/{name}", tags=["careers"],
                     description="Endpoint para obtener una carrera específica por su nombre",
                     response_model=CareerResponse)
async def get_career_by_name(name: str, db: Session = Depends(get_db)) -> dict[str, object]:
    career = search_by_name_service(db, name)
    # Si no encuentra la carrera, devolver un mensaje de error
    if not career:
        return {"message": "Carrera no encontrada"}
    return {"message": "Carrera encontrada", "career": career}

@career_controller.post("/careers", tags=["careers"],
                      description="Endpoint para crear una nueva carrera en el sistema",
                      response_model=CareerResponse)
async def create_career(
    career: CareerCreate, db: Session = Depends(get_db)
    ) -> dict[str, CareerResponse] | dict[str, object]:
    # Bloque de validacion
    try:
        created_career = create_career_service(career, db)
        if not created_career:
            return {"message": "Error al crear la carrera", "career": None}
        
        career_response = CareerResponse.model_validate(created_career)
        return {"message": "Carrera creada", "career": career_response}
    except Exception as e:
        return {"message": "Error al crear la carrera", "error": str(e)}

@career_controller.put("/careers/{id}", tags=["careers"],
                     description="Endpoint para actualizar una carrera específico por su ID",
                     response_model=CareerResponse)
async def update_career(
    id: int, career: CareerUpdate, db: Session = Depends(get_db)
    ) -> dict[str, CareerResponse] | dict[str, object]:
    # Bloque de validacion
    try:
        updated_career = update_career_service(id, career, db)
        if not updated_career:
            return {"message": "Carrera no encontrada o no pudo ser actualizada", "career": None}
        
        career_response = CareerResponse.model_validate(updated_career)
        return {"message": "Carrera actualizada", "career": career_response}
    except Exception as e:
        return {"message": "Error al actualizar la carrera", "error": str(e)}

@career_controller.delete("/careers/{id}", tags=["careers"],
                        description="Endpoint para eliminar una carrera específica por su ID")
async def delete_career(id: int, db: Session = Depends(get_db)) -> dict[str, object]:
    # Borrado logico, no definitivo
    success = delete_career_service(id, db)
    if success:
        return {"message": "Carrera eliminada exitosamente"}
    else:
        return {"message": "Carrera no encontrada o no pudo ser eliminada"}

@career_controller.post("/careers/{id}/reactivate", tags=["careers"],
                        description="Endpoint para reactivar una carrera específica por su ID",
                        response_model=CareerResponse)
async def reactivate_career(id: int, db: Session = Depends(get_db)) -> dict[str, object]:
    try:
        career = reactivate_career_service(id, db)
        if not career:
            return {"message": "Carrera no encontrada o no pudo ser reactivada", "career": None}
        
        career_response = CareerResponse.model_validate(career)
        return {"message": "Carrera reactivada", "career": career_response}
    except Exception as e:
        return {"message": "Error al reactivar la carrera", "error": str(e)}

@career_controller.delete("/careers/{id}/destroy", tags=["careers"],
                        description="Endpoint para eliminar definitivamente una carrera específica por su ID")
async def destroy_career(id: int, db: Session = Depends(get_db)) -> dict[str, object]:
    try:
        # Borrado definitivo
        success = destroy_career_service(id, db)
        if success:
            return {"message": "Carrera eliminada definitivamente"}
        else:
            return {"message": "Carrera no encontrada o no pudo ser eliminada definitivamente"}
    except Exception as e:
        return {"message": "Error al eliminar definitivamente la carrera", "error": str(e)}
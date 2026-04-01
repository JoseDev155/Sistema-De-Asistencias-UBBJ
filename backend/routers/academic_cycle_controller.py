# Librerias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from services import (
    create_academic_cycle_service,
    destroy_academic_cycle_service,
    get_all_academic_cycles as get_all_service,
    search_academic_cycle_by_id as search_by_id_service,
    search_academic_cycle_by_name as search_by_name_service,
    update_academic_cycle_service
)
from schemas import AcademicCycleCreate, AcademicCycleResponse, AcademicCycleUpdate
from database import get_db
from models import User
from utils import get_current_admin_user, get_current_professor_or_admin_user


# Instancia del router de ciclos académicos
academic_cycle_controller = APIRouter()


# RUTAS DE CICLOS ACADÉMICOS - SOLO ADMIN
@academic_cycle_controller.get("/academic-cycles", tags=["academic-cycles"],
                               description="Endpoint para obtener todos los ciclos académicos del sistema. Admin y Profesor.",
                               response_model=list[AcademicCycleResponse])
async def get_academic_cycles(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    cycles_list = get_all_service(db)
    return {"message": "Lista de ciclos académicos", "cycles": cycles_list}

@academic_cycle_controller.get("/academic-cycles/{id}", tags=["academic-cycles"],
                               description="Endpoint para obtener un ciclo académico específico por su ID. Admin y Profesor.",
                               response_model=AcademicCycleResponse)
async def get_academic_cycle(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    cycle = search_by_id_service(db, id)
    if not cycle:
        return {"message": "Ciclo académico no encontrado"}
    return {"message": "Ciclo académico encontrado", "cycle": cycle}

@academic_cycle_controller.get("/academic-cycles/search/{name}", tags=["academic-cycles"],
                               description="Endpoint para obtener un ciclo académico específico por su nombre. Admin y Profesor.",
                               response_model=AcademicCycleResponse)
async def get_academic_cycle_by_name(
    name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    cycle = search_by_name_service(db, name)
    if not cycle:
        return {"message": "Ciclo académico no encontrado"}
    return {"message": "Ciclo académico encontrado", "cycle": cycle}

@academic_cycle_controller.post("/academic-cycles", tags=["academic-cycles"],
                                description="Endpoint para crear un nuevo ciclo académico en el sistema. Solo Admin.",
                                response_model=AcademicCycleResponse)
async def create_academic_cycle(
    cycle: AcademicCycleCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, AcademicCycleResponse] | dict[str, object]:
    try:
        created_cycle = create_academic_cycle_service(cycle, db)
        if not created_cycle:
            return {"message": "Error al crear el ciclo académico", "cycle": None}
        
        cycle_response = AcademicCycleResponse.model_validate(created_cycle)
        return {"message": "Ciclo académico creado", "cycle": cycle_response}
    except Exception as e:
        return {"message": "Error al crear el ciclo académico", "error": str(e)}

@academic_cycle_controller.put("/academic-cycles/{id}", tags=["academic-cycles"],
                               description="Endpoint para actualizar un ciclo académico específico por su ID. Solo Admin.",
                               response_model=AcademicCycleResponse)
async def update_academic_cycle(
    id: int,
    cycle: AcademicCycleUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, AcademicCycleResponse] | dict[str, object]:
    try:
        updated_cycle = update_academic_cycle_service(id, cycle, db)
        if not updated_cycle:
            return {"message": "Ciclo académico no encontrado o no pudo ser actualizado", "cycle": None}
        
        cycle_response = AcademicCycleResponse.model_validate(updated_cycle)
        return {"message": "Ciclo académico actualizado", "cycle": cycle_response}
    except Exception as e:
        return {"message": "Error al actualizar el ciclo académico", "error": str(e)}

@academic_cycle_controller.delete("/academic-cycles/{id}", tags=["academic-cycles"],
                                  description="Endpoint para eliminar un ciclo académico específico por su ID. Solo Admin.")
async def delete_academic_cycle(
    id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    success = destroy_academic_cycle_service(id, db)
    if success:
        return {"message": "Ciclo académico eliminado exitosamente"}
    else:
        return {"message": "Ciclo académico no encontrado o no pudo ser eliminado"}

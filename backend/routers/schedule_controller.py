# Librerias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from services import (
    create_schedule_service,
    destroy_schedule_service,
    get_all_schedules as get_all_service,
    search_schedules_by_day as search_by_day_service,
    search_schedule_by_id as search_by_id_service,
    update_schedule_service
)
from schemas import ScheduleCreate, ScheduleResponse, ScheduleUpdate
from database import get_db
from models import User
from utils import get_current_admin_user, get_current_professor_or_admin_user


# Instancia del router de horarios
schedule_controller = APIRouter()


# RUTAS DE HORARIOS - SOLO ADMIN
@schedule_controller.get("/schedules", tags=["schedules"],
                        description="Endpoint para obtener todos los horarios del sistema. Admin y Profesor.",
                        response_model=list[ScheduleResponse])
async def get_schedules(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    schedules_list = get_all_service(db)
    return {"message": "Lista de horarios", "schedules": schedules_list}

@schedule_controller.get("/schedules/{id}", tags=["schedules"],
                        description="Endpoint para obtener un horario específico por su ID. Admin y Profesor.",
                        response_model=ScheduleResponse)
async def get_schedule(
    id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    schedule = search_by_id_service(db, id)
    if not schedule:
        return {"message": "Horario no encontrado"}
    return {"message": "Horario encontrado", "schedule": schedule}

@schedule_controller.get("/schedules/search/{day}", tags=["schedules"],
                        description="Endpoint para obtener un horario específico por día de la semana. Admin y Profesor.",
                        response_model=ScheduleResponse)
async def get_schedule_by_day(
    day: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    schedule = search_by_day_service(db, day)
    if not schedule:
        return {"message": "Horario no encontrado"}
    return {"message": "Horario encontrado", "schedule": schedule}

@schedule_controller.post("/schedules", tags=["schedules"],
                         description="Endpoint para crear un nuevo horario en el sistema. Solo Admin.",
                         response_model=ScheduleResponse)
async def create_schedule(
    schedule: ScheduleCreate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, ScheduleResponse] | dict[str, object]:
    try:
        created_schedule = create_schedule_service(schedule, db)
        if not created_schedule:
            return {"message": "Error al crear el horario", "schedule": None}
        
        schedule_response = ScheduleResponse.model_validate(created_schedule)
        return {"message": "Horario creado", "schedule": schedule_response}
    except Exception as e:
        return {"message": "Error al crear el horario", "error": str(e)}

@schedule_controller.put("/schedules/{id}", tags=["schedules"],
                        description="Endpoint para actualizar un horario específico por su ID. Solo Admin.",
                        response_model=ScheduleResponse)
async def update_schedule(
    id: str,
    schedule: ScheduleUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, ScheduleResponse] | dict[str, object]:
    try:
        updated_schedule = update_schedule_service(id, schedule, db)
        if not updated_schedule:
            return {"message": "Horario no encontrado o no pudo ser actualizado", "schedule": None}
        
        schedule_response = ScheduleResponse.model_validate(updated_schedule)
        return {"message": "Horario actualizado", "schedule": schedule_response}
    except Exception as e:
        return {"message": "Error al actualizar el horario", "error": str(e)}

@schedule_controller.delete("/schedules/{id}", tags=["schedules"],
                           description="Endpoint para eliminar un horario específico por su ID. Solo Admin.")
async def delete_schedule(
    id: str,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    success = destroy_schedule_service(id, db)
    if success:
        return {"message": "Horario eliminado exitosamente"}
    else:
        return {"message": "Horario no encontrado o no pudo ser eliminado"}

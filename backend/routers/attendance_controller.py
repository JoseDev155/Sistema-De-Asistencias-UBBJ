# Librerias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from services import (
    create_attendance_service,
    destroy_attendance_service,
    get_all_attendances as get_all_service,
    search_attendance_by_id as search_by_id_service,
    update_attendance_service
)
from schemas import AttendanceCreate, AttendanceResponse, AttendanceUpdate
from database import get_db
from models import User
from utils import get_current_professor_or_admin_user, get_current_admin_user


# Instancia del router de asistencias
attendance_controller = APIRouter()


# RUTAS DE ASISTENCIAS - Admin y Profesor  
@attendance_controller.get("/attendances", tags=["attendances"],
                          description="Endpoint para obtener todas las asistencias del sistema. Admin y Profesor.",
                          response_model=list[AttendanceResponse])
async def get_attendances(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    attendances_list = get_all_service(db)
    return {"message": "Lista de asistencias", "attendances": attendances_list}


@attendance_controller.get("/attendances/{id}", tags=["attendances"],
                          description="Endpoint para obtener una asistencia específica por su ID. Admin y Profesor.",
                          response_model=AttendanceResponse)
async def get_attendance(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, object]:
    attendance = search_by_id_service(db, id)
    if not attendance:
        return {"message": "Asistencia no encontrada"}
    return {"message": "Asistencia encontrada", "attendance": attendance}


@attendance_controller.post("/attendances", tags=["attendances"],
                           description="Endpoint para crear una nueva asistencia en el sistema. Admin y Profesor.",
                           response_model=AttendanceResponse)
async def create_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_professor_or_admin_user)
) -> dict[str, AttendanceResponse] | dict[str, object]:
    try:
        created_attendance = create_attendance_service(attendance, db)
        if not created_attendance:
            return {"message": "Error al crear la asistencia", "attendance": None}
        
        attendance_response = AttendanceResponse.model_validate(created_attendance)
        return {"message": "Asistencia creada", "attendance": attendance_response}
    except Exception as e:
        return {"message": "Error al crear la asistencia", "error": str(e)}


@attendance_controller.put("/attendances/{id}", tags=["attendances"],
                          description="Endpoint para actualizar una asistencia específica por su ID. Solo Admin.",
                          response_model=AttendanceResponse)
async def update_attendance(
    id: int,
    attendance: AttendanceUpdate,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, AttendanceResponse] | dict[str, object]:
    try:
        updated_attendance = update_attendance_service(id, attendance, db)
        if not updated_attendance:
            return {"message": "Asistencia no encontrada o no pudo ser actualizada", "attendance": None}
        
        attendance_response = AttendanceResponse.model_validate(updated_attendance)
        return {"message": "Asistencia actualizada", "attendance": attendance_response}
    except Exception as e:
        return {"message": "Error al actualizar la asistencia", "error": str(e)}


@attendance_controller.delete("/attendances/{id}", tags=["attendances"],
                             description="Endpoint para eliminar una asistencia específica por su ID. Solo Admin.")
async def delete_attendance(
    id: int,
    db: Session = Depends(get_db),
    current_admin: User = Depends(get_current_admin_user)
) -> dict[str, object]:
    success = destroy_attendance_service(id, db)
    if success:
        return {"message": "Asistencia eliminada exitosamente"}
    else:
        return {"message": "Asistencia no encontrada o no pudo ser eliminada"}

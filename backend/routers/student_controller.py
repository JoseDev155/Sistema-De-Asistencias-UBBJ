# Librerias
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from services import (
    create_student_service, \
    destroy_student_service, \
    get_all_students as get_all_service, \
    search_students_by_email as search_by_email_service, \
    search_student_by_id as search_by_id_service, \
    search_students_by_name as search_by_name_service, \
    update_student_service)
from schemas import StudentCreate, StudentResponse, StudentUpdate
from database import get_db


# Instancia del router de estudiantes
student_controller = APIRouter()


# RUTAS DE ESTUDIANTES
@student_controller.get("/students", tags=["students"],
                       description="Endpoint para obtener todos los estudiantes del sistema",
                       response_model=list[StudentResponse])
async def get_students(db: Session = Depends(get_db)) -> dict[str, object]:
    students_list = get_all_service(db)
    return {"message": "Lista de estudiantes", "students": students_list}

@student_controller.get("/students/{id}", tags=["students"],
                       description="Endpoint para obtener un estudiante específico por su ID",
                       response_model=StudentResponse)
async def get_student(id: str, db: Session = Depends(get_db)) -> dict[str, object]:
    student = search_by_id_service(db, id)
    if not student:
        return {"message": "Estudiante no encontrado"}
    return {"message": "Estudiante encontrado", "student": student}

@student_controller.get("/students/search/name/{name}", tags=["students"],
                       description="Endpoint para obtener un estudiante específico por su nombre",
                       response_model=StudentResponse)
async def get_student_by_name(name: str, db: Session = Depends(get_db)) -> dict[str, object]:
    student = search_by_name_service(db, name)
    if not student:
        return {"message": "Estudiante no encontrado"}
    return {"message": "Estudiante encontrado", "student": student}

@student_controller.get("/students/search/email/{email}", tags=["students"],
                       description="Endpoint para obtener un estudiante específico por su email",
                       response_model=StudentResponse)
async def get_student_by_email(email: str, db: Session = Depends(get_db)) -> dict[str, object]:
    student = search_by_email_service(db, email)
    if not student:
        return {"message": "Estudiante no encontrado"}
    return {"message": "Estudiante encontrado", "student": student}

@student_controller.post("/students", tags=["students"],
                        description="Endpoint para crear un nuevo estudiante en el sistema",
                        response_model=StudentResponse)
async def create_student(
    student: StudentCreate, db: Session = Depends(get_db)
    ) -> dict[str, StudentResponse] | dict[str, object]:
    try:
        created_student = create_student_service(student, db)
        if not created_student:
            return {"message": "Error al crear el estudiante", "student": None}
        
        student_response = StudentResponse.model_validate(created_student)
        return {"message": "Estudiante creado", "student": student_response}
    except Exception as e:
        return {"message": "Error al crear el estudiante", "error": str(e)}

@student_controller.put("/students/{id}", tags=["students"],
                       description="Endpoint para actualizar un estudiante específico por su ID",
                       response_model=StudentResponse)
async def update_student(
    id: str, student: StudentUpdate, db: Session = Depends(get_db)
    ) -> dict[str, StudentResponse] | dict[str, object]:
    try:
        updated_student = update_student_service(id, student, db)
        if not updated_student:
            return {"message": "Estudiante no encontrado o no pudo ser actualizado", "student": None}
        
        student_response = StudentResponse.model_validate(updated_student)
        return {"message": "Estudiante actualizado", "student": student_response}
    except Exception as e:
        return {"message": "Error al actualizar el estudiante", "error": str(e)}

@student_controller.delete("/students/{id}", tags=["students"],
                          description="Endpoint para eliminar un estudiante específico por su ID")
async def delete_student(id: str, db: Session = Depends(get_db)) -> dict[str, object]:
    success = destroy_student_service(id, db)
    if success:
        return {"message": "Estudiante eliminado exitosamente"}
    else:
        return {"message": "Estudiante no encontrado o no pudo ser eliminado"}

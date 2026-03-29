# Archivo principal de la aplicacion FastAPI

# Librerias
from fastapi import FastAPI
# Importar directorios del proyecto
from routers import (
    academic_cycle_controller, \
    attendance_controller, \
#    auth_controller, \
    career_controller, \
    career_signature_controller, \
    enrollment_controller, \
    group_controller, \
    role_controller, \
    schedule_controller, \
    signature_controller, \
    student_controller, \
    user_controller)

# Crear una instancia de FastAPI
app = FastAPI()
# Agregar los controladores a la API
app.include_router(academic_cycle_controller)
app.include_router(attendance_controller)
#app.include_router(auth_controller)
app.include_router(career_controller)
app.include_router(career_signature_controller)
app.include_router(enrollment_controller)
app.include_router(group_controller)
app.include_router(role_controller)
app.include_router(schedule_controller)
app.include_router(signature_controller)
app.include_router(student_controller)
app.include_router(user_controller)


# Ruta base de la API
@app.get("/")
async def hello():
    return {"message": "Hello, World!"}
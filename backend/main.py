from fastapi import FastAPI
from routers.user_controller import user_controller
from routers.auth_controller import auth_controller

# Crear una instancia de FastAPI
app = FastAPI()
# Agregar los controladores a la API
app.include_router(user_controller)
app.include_router(auth_controller)

# Ruta base de la API
@app.get("/")
async def hello():
    return {"message": "Hello, World!"}
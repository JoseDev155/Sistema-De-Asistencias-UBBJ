# Librerias
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from database import get_db
from models import User
from utils import get_current_user
from services import (
    login_auth_service,
    register_auth_service,
    refresh_token_auth_service,
    change_password_auth_service,
    get_current_user_info_service
)
from schemas import (
    LoginRequest, RegisterRequest, ChangePasswordRequest, RefreshTokenRequest,
    TokenResponse, UserResponse
)

# Instancia del router de autenticación
auth_controller = APIRouter(prefix="/auth", tags=["Autenticación"])


# RUTAS DE AUTENTICACION
@auth_controller.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    """
    **Login de usuario**
    
    Autentica un usuario usando ID o email y contraseña.
    Retorna access_token y refresh_token.
    
    - **username**: ID del usuario o email
    - **password**: Contraseña del usuario
    """
    return login_auth_service(db, login_data)


@auth_controller.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(
    register_data: RegisterRequest,
    db: Session = Depends(get_db)
):
    """
    **Registro de nuevo usuario**
    
    Crea un nuevo usuario en el sistema.
    Las contraseñas deben ser iguales y mínimo 8 caracteres.
    
    - **id**: ID único del usuario (máximo 15 caracteres)
    - **first_name**: Nombre del usuario
    - **last_name**: Apellido del usuario
    - **email**: Email único
    - **password**: Contraseña (mínimo 8 caracteres)
    - **password_confirm**: Confirmación de contraseña
    - **role_id**: ID del rol (1=Admin, 2=Profesor, 3=Estudiante)
    """
    return register_auth_service(db, register_data)


@auth_controller.post("/refresh", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def refresh_access_token(refresh_data: RefreshTokenRequest):
    """
    **Renovar access token**
    
    Genera un nuevo access_token usando un refresh_token válido.
    El refresh_token debe estar vigente.
    """
    return refresh_token_auth_service(refresh_data.refresh_token)


@auth_controller.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_me(current_user: User = Depends(get_current_user)):
    """
    **Obtener información del usuario actual**
    
    Retorna los datos del usuario autenticado.
    Requiere token válido.
    """
    return get_current_user_info_service(current_user)


@auth_controller.post("/change-password", status_code=status.HTTP_200_OK)
async def change_password(
    change_pwd_data: ChangePasswordRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    **Cambiar contraseña**
    
    Permite al usuario cambiar su contraseña.
    Requiere la contraseña actual para validación.
    
    - **current_password**: Contraseña actual
    - **new_password**: Nueva contraseña (mínimo 8 caracteres)
    - **password_confirm**: Confirmación de nueva contraseña
    """
    return change_password_auth_service(db, current_user, change_pwd_data)
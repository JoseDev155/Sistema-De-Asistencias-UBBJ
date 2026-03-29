# Librerias
from fastapi import Depends
from sqlalchemy.orm import Session
# Importar directorios del proyecto
from repositories import user_search_by_name as search_by_name
from database import get_db
from models import User
from utils import verify_password

def login_auth_service(db: Session = Depends(get_db), name: str | None = None,
                             password: str | None = None) -> User | None:
    if not name or not password:
        return None
    else:
        user_name = name
        user_password = password
        user: User = search_by_name(db, user_name)
    
    if not user:
        return None
    
    if not verify_password(user_password, user.password):
        return None

    return user
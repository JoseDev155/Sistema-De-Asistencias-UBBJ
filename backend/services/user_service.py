# Librerias
#from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import List
# Importar directorios del proyecto
from repositories import (
    user_get_all as get_all, \
    user_search_by_id as search_by_id, \
    user_search_by_id_or_email as search_by_id_or_email, \
    user_create as create, \
    user_update as update)
from database import get_db
from models import User
from schemas import UserCreate, UserUpdate
from utils import get_password_hash


#oauth2 = OAuth2PasswordBearer(tokenUrl="token")

def get_all_service(db: Session = Depends(get_db)) -> List[User]:
    return get_all(db)

def search_by_id_service(db: Session = Depends(get_db), id: str | None = None) -> User | None:
    if not id:
        return None
    return search_by_id(db, id)

def search_by_id_or_email_service(db: Session = Depends(get_db), id: str | None = None, email: str | None = None) -> User | None:
    if not id and not email:
        return None
    return search_by_id_or_email(db, id, email)

def create_user_service(user: UserCreate, db: Session = Depends(get_db)) -> User | None:
    hash_pass = get_password_hash(user.password)
    try:
        new_user = create(db, id=user.id, first_name=user.first_name, last_name=user.last_name,
                                   email=user.email, password=hash_pass, role_id=user.role_id, is_active=True)
        return new_user
    except Exception as e:
        # Log error
        print(f"Error creating user: {e}")
        return None

def update_user_service(user_id: str, user_update: UserUpdate,
                        db: Session = Depends(get_db)) -> User | None:
    try:
        updated_user = update(db, id=user_id, first_name=user_update.first_name,
                                   last_name=user_update.last_name, email=user_update.email)
        return updated_user
    except Exception as e:
        # Log error
        print(f"Error updating user: {e}")
        return None

def delete_user_service(user_id: str, db: Session = Depends(get_db)) -> bool:
    try:
        user = search_by_id(db, user_id)
        if not user:
            return False
        
        user.is_active = False
        db.commit()
        db.refresh(user)
        
        return True
    except Exception as e:
        # Log error
        print(f"Error deleting user: {e}")
        return False
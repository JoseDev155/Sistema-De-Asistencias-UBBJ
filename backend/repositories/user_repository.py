from sqlalchemy.orm import Session
from models.user import User


# Tipos opcionales
opt_str = str | None
opt_int = int | None
opt_bool = bool | None


# Metodos
def get_users(db: Session):
    return db.query(User).all()

def search_user_by_name(db: Session, first_name: str):
    return db.query(User).filter(User.first_name == first_name).first()

def create_user(db: Session, id: str, first_name: str, last_name: str, email: str, password: str,
                role_id: int, is_active: bool):
    # Crear una nueva instancia del modelo User con los datos proporcionados
    user = User(
        id=id,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        role_id=role_id,
        is_active=is_active
    )
    
    # Agregar el nuevo usuario
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

def update_user(db: Session, id: str, first_name: opt_str = None, last_name: opt_str = None, 
                email: opt_str = None, password: opt_str = None, role_id: opt_int = None,
                is_active: opt_bool = None):
    # Buscar el usuario por id
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        return None
    
    # Actualizar solo los campos que fueron proporcionados
    if first_name is not None:
        user.first_name = first_name
    if last_name is not None:
        user.last_name = last_name
    if email is not None:
        user.email = email
    if password is not None:
        user.password = password
    if role_id is not None:
        user.role_id = role_id
    if is_active is not None:
        user.is_active = is_active
    
    # Guardar los cambios
    db.commit()
    db.refresh(user)
    
    return user

def delete_user(db: Session, id: str):
    # Buscar el usuario por id
    user = db.query(User).filter(User.id == id).first()
    
    if not user:
        return None
    
    # Eliminar el usuario
    db.delete(user)
    db.commit()
    
    return user


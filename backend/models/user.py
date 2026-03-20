from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.connection import Base

# Modelo de usuario para la base de datos
class User(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "users"
    
    id = Column(String(15), primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    
    # Opcional, pero:
    # Relacion con el modelo de rol para SQLAlchemy
    role = relationship("Role", back_populates="users")
    
    # Recomendado para relaciones inversas entre tablas
    #user = relationship("User", back_populates="roles")
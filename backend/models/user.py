from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config.connection import Base

# Modelo de usuario para la base de datos
class User(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "users"

    id = Column(String(15), primary_key=True, index=True)
    names = Column(String(100), nullable=False)
    last_names = Column(String(100), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    id_role = Column(Integer, ForeignKey("roles.id"), nullable=False)
    is_active = Column(Boolean, nullable=False)
    
    # Opcional
    role = relationship("Role", back_populates="users")
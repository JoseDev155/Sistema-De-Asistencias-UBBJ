from sqlalchemy import Column, Integer, Boolean, String
from sqlalchemy.orm import relationship
from config.connection import Base

# Modelo de usuario para la base de datos
class Role(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "roles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    
    # Relacion inversa para SQLAlchemy
    users = relationship("User", back_populates="roles")
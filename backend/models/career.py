from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from config.connection import Base

# Modelo de carrera para la base de datos
class Career(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "careers"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    
    # Relacion inversa para SQLAlchemy
    signature_career = relationship("SignatureCareer", back_populates="careers")
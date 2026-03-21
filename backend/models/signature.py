from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from database.connection import Base

# Modelo de materia para la base de datos
class Signature(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "signatures"

    id = Column(String(15), primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    
    # Relacion inversa para SQLAlchemy
    career_signatures = relationship("CareerSignature", back_populates="signatures")
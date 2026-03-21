from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from database.connection import Base

# Modelo de carrera-asignatura para la base de datos
class CareerSignature(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "career_signatures"
    
    id = Column(String(15), primary_key=True)
    signature_id = Column(String(15), ForeignKey("signatures.id"))
    career_id = Column(String(15), ForeignKey("careers.id"))
    
    # Relacion inversa para SQLAlchemy
    group = relationship("Group", back_populates="career_signatures")
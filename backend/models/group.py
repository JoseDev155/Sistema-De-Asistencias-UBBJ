from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from config.connection import Base

# Modelo de grupo para la base de datos
class Group(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "groups"
    
    id = Column(String(15), primary_key=True)
    name = Column(String(15), nullable=False) # Ej: "A", "B" o "101"
    user_id = Column(String(15), ForeignKey("users.id")) # El profesor a cargo del grupo
    signature_c_id = Column(String(20), ForeignKey("signature_careers.id")) # La materia
    academic_cy_id = Column(Integer, ForeignKey("academic_cycles.id")) # El ciclo academico
    
    # Relaciones
    signature_career = relationship("SignatureCareer", back_populates="groups")
    user = relationship("User", back_populates="groups")
    academic_cycle = relationship("AcademicCycle", back_populates="groups")
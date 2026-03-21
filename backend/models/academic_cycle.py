from sqlalchemy import Column, Integer, Date, String
from sqlalchemy.orm import relationship
from database.connection import Base

# Modelo de usuario para la base de datos
class AcademicCycle(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "academic_cycles"
    
    id = Column(Integer, primary_key=True, index=True)
    cycle_name = Column(String(100), nullable=False)
    cycle_year = Column(Date, nullable=False)
    
    # Relacion con el modelo de rol para SQLAlchemy
    group = relationship("Group", back_populates="academic_cycles")
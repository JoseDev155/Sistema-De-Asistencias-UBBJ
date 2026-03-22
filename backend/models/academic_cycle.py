from sqlalchemy import Integer, Date, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.connection import Base

# Modelo de ciclo academico para la base de datos
class AcademicCycle(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "academic_cycles"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    cycle_name: Mapped[str] = mapped_column(String(100), nullable=False)
    cycle_year: Mapped[Date] = mapped_column(Date, nullable=False)
    
    # Relacion con el modelo de grupo para SQLAlchemy
    groups = relationship("Group", back_populates="academic_cycle")
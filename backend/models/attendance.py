from sqlalchemy import Column, Integer, DateTime, Enum, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

# Modelo de usuario para la base de datos
class Attendance(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "attendances"
    
    id = Column(Integer, primary_key=True, index=True)
    arrival_time = Column(DateTime, nullable=False)
    status = Column(
        Enum("present", "absent", "late", "justified", "left_early"),
        nullable=False)
    notes = Column(String(255), nullable=True)
    enrollment_id = Column(Integer, ForeignKey("enrollments.id"), nullable=False)
    
    # Relacion con el modelo de rol para SQLAlchemy
    enrollment = relationship("Enrollment", back_populates="attendances")
from sqlalchemy import Integer, DateTime, Enum, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from database.connection import Base

# Modelo de asistencia para la base de datos
class Attendance(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "attendances"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    arrival_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    status: Mapped[str] = mapped_column(
        Enum("present", "absent", "late", "justified", "left_early"),
        nullable=False)
    notes: Mapped[str | None] = mapped_column(String(255), nullable=True)
    enrollment_id: Mapped[int] = mapped_column(Integer, ForeignKey("enrollments.id"), nullable=False)
    
    # Relacion con el modelo de inscripcion para SQLAlchemy
    enrollment = relationship("Enrollment", back_populates="attendances")
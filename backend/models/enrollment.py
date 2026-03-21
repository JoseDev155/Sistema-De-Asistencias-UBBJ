from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

# Modelo de incsripciones para la base de datos
class Enrollment(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "enrollments"
    
    id = Column(Integer, primary_key=True)
    enrollment_date = Column(Date, nullable=False)
    student_id = Column(String(15), ForeignKey("students.id"), nullable=False)
    group_id = Column(String(15), ForeignKey("groups.id"), nullable=False)
    
    # Relacion inversa para SQLAlchemy
    student = relationship("Enrollment", back_populates="students")
    group = relationship("Enrollment", back_populates="groups")
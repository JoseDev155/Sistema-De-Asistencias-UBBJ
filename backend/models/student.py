from sqlalchemy import Column, String, Date, Boolean
from sqlalchemy.orm import relationship
from database.connection import Base

# Modelo de estudiante para la base de datos
class Student(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "students"
    
    id = Column(String(15), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    enrollment_date = Column(Date, nullable=False)
    is_active = Column(Boolean, default=True)
    
    # Relacion inversa para SQLAlchemy
    enrollment = relationship("Enrollment", back_populates="students")
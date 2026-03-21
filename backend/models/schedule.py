from sqlalchemy import Column, Integer, SmallInteger, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

# Modelo de usuario para la base de datos
class Schedule(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, index=True)
    day_of_week = Column(SmallInteger, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    max_entry_minutes = Column(SmallInteger, nullable=False)
    minutes_to_be_present = Column(SmallInteger, nullable=False, default=True)
    group_id = Column(String, ForeignKey("groups.id"), nullable=False)
    
    # Relacion con el modelo de grupo para SQLAlchemy
    group = relationship("Group", back_populates="schedules")
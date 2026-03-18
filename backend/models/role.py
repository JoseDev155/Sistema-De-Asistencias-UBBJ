from sqlalchemy import Column, Integer, SmallInteger, String
from config.connection import Base

# Modelo de usuario para la base de datos
class Role(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    status = Column(SmallInteger, nullable=False)
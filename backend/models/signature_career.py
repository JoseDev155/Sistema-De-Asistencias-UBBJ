from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from config.connection import Base

# Modelo de materia para la base de datos
class SignatureCareer(Base):
    # Nombre de la tabla en la base de datos
    __tablename__ = "signature_career"
    
    id = Column(String(15), primary_key=True)
    signature_id = Column(String(15), ForeignKey("signatures.id"))
    career_id = Column(String(15), ForeignKey("careers.id"))
    
    # Relacion inversa para SQLAlchemy
    group = relationship("Group", back_populates="signature_careers")
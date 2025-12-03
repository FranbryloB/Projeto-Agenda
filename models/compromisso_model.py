from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.db import Base

class Compromisso(Base):
    __tablename__ = "compromissos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    data = Column(String, nullable=False)  
    hora = Column(String, nullable=False)
    descricao = Column(String)
    concluido = Column(Boolean, default=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    usuario = relationship("Usuario", backref="compromissos")

    def __repr__(self):
        return f"<Compromisso {self.titulo}>"

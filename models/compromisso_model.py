from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base, engine, SessionLocal
from models.usuario_model import Usuario

class Compromisso(Base):
    __tablename__ = "compromissos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    data = Column(String, nullable=False)
    hora = Column(String, nullable=False)
    descricao = Column(String)
    concluido = Column(Boolean, default=False)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario")


def adicionar_compromisso(titulo, data, hora, descricao, usuario_id):
    session = SessionLocal()
    novo = Compromisso(
        titulo=titulo,
        data=data,
        hora=hora,
        descricao=descricao,
        usuario_id=usuario_id
    )
    session.add(novo)
    session.commit()
    session.close()


def listar_compromissos(usuario_id):
    session = SessionLocal()
    compromissos = session.query(Compromisso).filter_by(usuario_id=usuario_id).all()
    session.close()
    return compromissos


def buscar_compromisso(id, usuario_id):
    session = SessionLocal()
    compromisso = session.query(Compromisso).filter_by(id=id, usuario_id=usuario_id).first()
    session.close()
    return compromisso


def editar_compromisso(id, titulo, data, hora, descricao, usuario_id):
    session = SessionLocal()
    compromisso = session.query(Compromisso).filter_by(id=id, usuario_id=usuario_id).first()
    if compromisso:
        compromisso.titulo = titulo
        compromisso.data = data
        compromisso.hora = hora
        compromisso.descricao = descricao
        session.commit()
    session.close()


def excluir_compromisso(id, usuario_id):
    session = SessionLocal()
    compromisso = session.query(Compromisso).filter_by(id=id, usuario_id=usuario_id).first()
    if compromisso:
        session.delete(compromisso)
        session.commit()
    session.close()


def marcar_concluido(id, usuario_id):
    session = SessionLocal()
    compromisso = session.query(Compromisso).filter_by(id=id, usuario_id=usuario_id).first()
    if compromisso:
        compromisso.concluido = True
        session.commit()
    session.close()


def desmarcar_concluido(id, usuario_id):
    session = SessionLocal()
    compromisso = session.query(Compromisso).filter_by(id=id, usuario_id=usuario_id).first()
    if compromisso:
        compromisso.concluido = False
        session.commit()
    session.close()


Base.metadata.create_all(bind=engine)

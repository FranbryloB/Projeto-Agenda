from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Conexão com SQLite
engine = create_engine("sqlite:///agenda.db", echo=False)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Compromisso(Base):
    __tablename__ = "compromissos"

    id = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    data = Column(String, nullable=False)
    hora = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    concluido = Column(Boolean, default=False)

Base.metadata.create_all(engine)

def adicionar_compromisso(titulo, data, hora, descricao):
    novo = Compromisso(
        titulo=titulo,
        data=data,
        hora=hora,
        descricao=descricao,
        concluido=False
    )
    session.add(novo)
    session.commit()

def listar_compromissos():
    return session.query(Compromisso).all()

def buscar_compromisso(id):
    return session.query(Compromisso).filter_by(id=id).first()

def editar_compromisso(id, titulo, data, hora, descricao):
    compromisso = buscar_compromisso(id)
    if compromisso:
        compromisso.titulo = titulo
        compromisso.data = data
        compromisso.hora = hora
        compromisso.descricao = descricao
        session.commit()

def excluir_compromisso(id):
    compromisso = buscar_compromisso(id)
    if compromisso:
        session.delete(compromisso)
        session.commit()

def marcar_concluido(id):
    compromisso = buscar_compromisso(id)
    if compromisso:
        compromisso.concluido = True
        session.commit()

def desmarcar_concluido(id):
    compromisso = buscar_compromisso(id)
    if compromisso:
        compromisso.concluido = False
        session.commit()

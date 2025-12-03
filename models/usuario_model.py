from sqlalchemy import Column, Integer, String
from database import Base, engine, SessionLocal

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    senha = Column(String, nullable=False)


def cadastrar_usuario(nome, email, senha):
    session = SessionLocal()
    usuario = Usuario(nome=nome, email=email, senha=senha)
    session.add(usuario)
    session.commit()
    session.close()


def buscar_usuario_por_email(email):
    session = SessionLocal()
    usuario = session.query(Usuario).filter_by(email=email).first()
    session.close()
    return usuario


# Cria tabela se não existir
Base.metadata.create_all(bind=engine)

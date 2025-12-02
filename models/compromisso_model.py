import sqlite3

DB_NAME = "agenda.db"

class Compromisso:
    def __init__(self, id, titulo, data, hora, descricao, concluido=0):
        self.id = id
        self.titulo = titulo
        self.data = data
        self.hora = hora
        self.descricao = descricao
        self.concluido = concluido

def criar_tabela_compromissos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS compromissos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            descricao TEXT,
            concluido BOOLEAN DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()


<<<<<<< HEAD
Base.metadata.create_all(engine)
=======
criar_tabela_compromissos()
>>>>>>> 6369eb98921337d1f2b65495f288b6c9120a9fcc

def adicionar_compromisso(titulo, data, hora, descricao):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO compromissos (titulo, data, hora, descricao, concluido) VALUES (?, ?, ?, ?, 0)",
        (titulo, data, hora, descricao)
    )
    conn.commit()
    conn.close()


def listar_compromissos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compromissos")
    rows = cursor.fetchall()
    conn.close()
    return [Compromisso(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]


def buscar_compromisso(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compromissos WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Compromisso(row[0], row[1], row[2], row[3], row[4], row[5])
    return None


def editar_compromisso(id, titulo, data, hora, descricao):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE compromissos SET titulo = ?, data = ?, hora = ?, descricao = ? WHERE id = ?",
        (titulo, data, hora, descricao, id)
    )
    conn.commit()
    conn.close()


def excluir_compromisso(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM compromissos WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def marcar_concluido(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE compromissos SET concluido = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()


def desmarcar_concluido(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("UPDATE compromissos SET concluido = 0 WHERE id = ?", (id,))
    conn.commit()
    conn.close()

import sqlite3

DB_NAME = "agenda.db"

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


criar_tabela_compromissos()

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
    compromissos = cursor.fetchall()
    conn.close()
    return compromissos


def buscar_compromisso(id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM compromissos WHERE id = ?", (id,))
    compromisso = cursor.fetchone()
    conn.close()
    return compromisso


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

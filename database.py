import sqlite3

def conectar():
    """Cria a conexão com o banco de dados SQLite."""
    return sqlite3.connect("clientes.db")

def criar_tabela():
    """Cria a tabela 'clientes' caso ela ainda não exista."""
    conexao = conectar()
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT
        )
    """)
    
    conexao.commit()
    conexao.close()

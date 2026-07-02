import sqlite3

def conectar():
    conexao = sqlite3.connect('ravache.db')
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telefone TEXT,
            autor TEXT,
            mensagem TEXT,
            data DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    conexao.COMMIT()
    conexao.close()

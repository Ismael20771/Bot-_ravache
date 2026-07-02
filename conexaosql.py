import sqlite3


def conectar():
    return sqlite3.connect("ravache.db")


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    # Tabela de mensagens
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mensagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telefone TEXT,
            autor TEXT,
            mensagem TEXT,
            data DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Tabela de contexto
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contexto (
            telefone TEXT PRIMARY KEY,
            assunto TEXT,
            etapa TEXT,
            ultima_msg TEXT,
            ultima_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexao.commit()
    conexao.close()


def salvar_mensagem(telefone, autor, mensagem):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO mensagens (telefone, autor, mensagem)
        VALUES (?, ?, ?)
    """, (telefone, autor, mensagem))

    conexao.commit()
    conexao.close()


def salvar_contexto(telefone, assunto, etapa, ultima_msg):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO contexto (telefone, assunto, etapa, ultima_msg)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(telefone)
        DO UPDATE SET
            assunto = excluded.assunto,
            etapa = excluded.etapa,
            ultima_msg = excluded.ultima_msg,
            ultima_atualizacao = CURRENT_TIMESTAMP
    """, (telefone, assunto, etapa, ultima_msg))

    conexao.commit()
    conexao.close()


def buscar_contexto(telefone):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT assunto, etapa, ultima_msg
        FROM contexto
        WHERE telefone = ?
    """, (telefone,))

    resultado = cursor.fetchone()

    conexao.close()

    return resultado
import sqlite3

def conexao():
    conectar = sqlite3.connect('tabela.db')
    return conectar

def criarTabela():
    conectar = conexao()
    cursor = conectar.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL)""")

# caso queira limpar os dados da tabela
def LimparTabela():
    conectar = conexao()
    cursor = conectar.cursor()
    cursor.execute('DELETE FROM users')

    conectar.commit()
    conectar.close()

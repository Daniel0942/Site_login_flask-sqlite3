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
    username TXT NOT NULL,
    password REAL NOT NULL)""")
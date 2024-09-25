import sqlite3

def conexao():
    conectar = sqlite3.connect('tabela.db')
    conectar.execute("PRAGMA foreign_keys = ON")
    return conectar

def criarTabela_users():
    conectar = conexao()
    cursor = conectar.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL)""")
    conectar.commit()
    conectar.close()

def criarTabela_gerenciador():
    conectar = conexao()
    cursor = conectar.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS gerenciador (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    valor REAL NOT NULL,
    quantidade INTEGER NOT NULL,
    id_user INTEGER,
    FOREIGN KEY (id_user) REFERENCES users(id))
    """)

    conectar.commit()
    conectar.close()

def InserirDadosFicticios():
    dadosFicticios = [
        {"produto": "Notebook", "preco": 3500.00, "quantidade": 5},
        {"produto": "Mouse", "preco": 120.00, "quantidade": 20},
        {"produto": "Teclado Mecânico", "preco": 300.00, "quantidade": 15},
        {"produto": "Monitor 24''", "preco": 800.00, "quantidade": 8},
        {"produto": "Headset Gamer", "preco": 250.00, "quantidade": 12},
        {"produto": "Smartphone", "preco": 2000.00, "quantidade": 7},
        {"produto": "Impressora", "preco": 600.00, "quantidade": 10},
        {"produto": "Cadeira Gamer", "preco": 900.00, "quantidade": 4},
        {"produto": "Pendrive 64GB", "preco": 40.00, "quantidade": 50},
        {"produto": "SSD 500GB", "preco": 400.00, "quantidade": 10}
        ]
    conectar = conexao()
    cursor = conectar.cursor()
    for dados in dadosFicticios:
        cursor.execute('INSERT INTO gerenciador (produto, valor, quantidade) VALUES (?, ?, ?)', (dados["produto"], dados["preco"], dados["quantidade"]))
    conectar.commit()
    conectar.close()

# caso queira limpar os dados da tabela
def LimparTabela():
    conectar = conexao()
    cursor = conectar.cursor()
    cursor.execute('DELETE FROM gerenciador')

    conectar.commit()
    conectar.close()


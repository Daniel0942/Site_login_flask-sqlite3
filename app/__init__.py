from flask import Flask, render_template, request, flash
from models.table import conexao, criarTabela_users, criarTabela_gerenciador
import sqlite3

app = Flask(__name__)
app.secret_key = "12345"      # necessário pra usar o flash

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar", methods = ["POST"])
def cadastrar():
    username = request.form["username"]
    password = request.form["password"]
    try:
        conectar = conexao()
        cursor = conectar.cursor()
        cursor.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, password))
        conectar.commit()
        flash("Usuário cadastrado com sucesso !")
        return render_template("produto.html")
    except sqlite3.IntegrityError:
        flash("[ERRO], Usuário já existe !")
    finally:
        conectar.close()
    return render_template("index.html")

@app.route("/formulario", methods = ["POST"])
def formulario():
    produto = request.form["produto"]
    valor = request.form["valor"]
    quantidade = request.form["quantidade"]
    try:
        conectar = conexao()
        cursor = conectar.cursor()
        cursor.execute('INSERT INTO gerenciador (produto, valor, quantidade) VALUES (?, ?, ?)', (produto, valor, quantidade))
        conectar.commit()
        cursor.close()
        flash("Produto cadastrado com sucesso")
    except :
        flash("[ERRO], Digite os dados novamente !")
    return render_template("produto.html")

if __name__ == "__main__":
    criarTabela_users()
    criarTabela_gerenciador()
    app.run(debug=True)  # "debug" é pra atualizações automáticas
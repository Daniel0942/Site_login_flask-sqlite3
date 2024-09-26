from flask import Flask, render_template, request, flash, session, redirect, url_for
from models.table import conexao, criarTabela_users, criarTabela_gerenciador
import sqlite3

app = Flask(__name__)
app.secret_key = "12345"      # necessário pra usar o flash

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    conectar = conexao()
    cursor = conectar.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conectar.close()

    if user:
        session["user_id"] = user[0]  # Armazena o ID do usuário na sessão
        flash("Login realizado com sucesso!")
        return render_template("produto.html")
    else:
        flash("[ERRO], Usuário ou senha incorretos!")
        return redirect(url_for("index"))

@app.route("/cadastrar_botao")
def cadastrar_botao():
    return render_template("cadastro.html")

@app.route("/logout")
def logout():
    session.pop("user_id", None)  # Remove a chave 'user_id' da sessão
    flash("Logout feito com sucesso !")
    return redirect(url_for("index"))

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
        return render_template("login.html")
    except sqlite3.IntegrityError:
        flash("[ERRO], Usuário já existe !")
    finally:
        conectar.close()
    return render_template("cadastro.html")

@app.route("/formulario", methods = ["POST"])
def formulario():
    produto = request.form["produto"]
    valor = request.form["valor"]
    quantidade = request.form["quantidade"]
    try:
        conectar = conexao()
        cursor = conectar.cursor()
        cursor.execute('INSERT INTO gerenciador (produto, valor, quantidade, id_user) VALUES (?, ?, ?, ?)', (produto, valor, quantidade, session["user_id"]))
        conectar.commit()
        cursor.close()
        flash("Produto cadastrado com sucesso")
    except sqlite3.Error as e:  # Captura erros do SQLite
        flash(f"[ERRO], Ocorreu um erro ao tentar adicionar o produto: {str(e)}")
    return render_template("produto.html")

if __name__ == "__main__":
    criarTabela_users()
    criarTabela_gerenciador()
    app.run(debug=True)  # "debug" é pra atualizações automáticas
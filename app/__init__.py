from flask import Flask, render_template, request
from models.table import conexao, criarTabela

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar", methods = ["POST"])
def cadastrar():
    username = request.form["username"]
    password = request.form["password"]

    conectar = conexao()
    cursor = conectar.cursor()
    cursor.execute("INSERT INTO users(username, password) VALUES(?, ?)", (username, password))

    conectar.commit()
    conectar.close()
    return render_template("index.html")

if __name__ == "__main__":
    criarTabela()
    app.run(debug=True)  # "debug" é pra atualizações automáticas
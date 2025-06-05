from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Página inicial redireciona para login
@app.route("/")
def home():
    return redirect(url_for("login"))

# Rota para tela de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Validação simples (em produção, use hash + banco seguro)
        if username == "admin" and password == "senha123":
            return f"<h2>Bem-vindo, {username}!</h2><p>Login realizado com sucesso.</p>"
        else:
            return "<h3>Usuário ou senha inválidos!</h3>", 401

    return render_template("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

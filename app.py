from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

carros_lancamentos = [
    {"nome": "Corolla", "detalhes": "2.0 Flex CVT", "preco": "R$ 149.990,00"},
    {"nome": "Civic", "detalhes": "2.0 Turbo", "preco": "R$ 189.990,00"},
    {"nome": "Pulse", "detalhes": "SUV Turbo 200", "preco": "R$ 108.490,00"},
]

carros_bmw = [
    {"nome": "Z4", "detalhes": "Roadster 2.0 Turbo", "preco": "R$ 399.900,00"},
    {"nome": "X1", "detalhes": "SUV xDrive 2.0", "preco": "R$ 279.900,00"},
    {"nome": "M5", "detalhes": "4.4 V8 Turbo", "preco": "R$ 1.199.900,00"},
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        carros_lancamentos=carros_lancamentos,
        carros_bmw=carros_bmw
    )



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        # Exemplo: validar usuário (substituir pela sua lógica)
        if email == "usuario" and password == "senha123":
            session["user"] = email
            return redirect(url_for("home"))
        else:
            flash("Usuário ou senha inválidos")
    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)
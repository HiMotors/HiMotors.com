import secrets
from flask import Flask, render_template, request, redirect, url_for, session, flash, abort

app = Flask(__name__)
app.secret_key = 'zagoda231'

carros_lancamentos = [
    {"nome": "Volkswagen Tera", "desc": "SUV 1.0 170 TSI", "preco": "R$ 141.890"},
    {"nome": "Chevrolet Onix", "desc": "Premier AT Turbo", "preco": "R$ 127.490"},
    {"nome": "Toyota Yaris Cross", "desc": "SUV Hybrid 130", "preco": "R$ 185.090"},
]

carros_bmw = [
    {"nome": "BMW i5", "desc": "M60 xDrive Sport", "preco": "R$ 759.950"},
    {"nome": "BMW X1", "desc": "SUV iDrive 8.0", "preco": "R$ 342.085"},
    {"nome": "BMW M5", "desc": "4.4 V8 xDrive", "preco": "R$ 811.540"},
]

@app.route("/")
def home():
    return render_template(
        "index.html",
        carros_lancamentos=carros_lancamentos,
        carros_bmw=carros_bmw
    )

@app.route('/detalhes/<nome>')
def carro_detalhes(nome):
    carro = next((c for c in carros_lancamentos if c['nome'].lower() == nome.lower()), None)
    if not carro:
        carro = next((c for c in carros_bmw if c['nome'].lower() == nome.lower()), None)
    if not carro:
        abort(404)

    car_img = f"/static/imgs/{carro['nome'].lower()}.jpg" 

    return render_template('detalhes.html', c=carro, car={'img': car_img, 'name': carro['nome']})


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == "usuario@gmail.com" and password == "senha123":
            session["user"] = email
            return redirect(url_for("home"))
        else:
            flash("Usuário ou senha inválidos")
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if not email or not password:
            flash('Por favor, preencha todos os campos')
            return redirect(url_for('register'))
        
        flash('Usuário registrado com sucesso!')
        return redirect(url_for('login'))
    
    return render_template('register.html')

if __name__ == "__main__":
    app.run(debug=True)
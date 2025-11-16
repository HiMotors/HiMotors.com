from flask import request, redirect, url_for, session, flash, render_template

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uid = request.form["uid"]
        password = request.form["password"]
        # Exemplo: validar usuário (substituir pela sua lógica)
        if uid == "usuario" and password == "senha123":
            session["user"] = uid
            return redirect(url_for("home"))
        else:
            flash("Usuário ou senha inválidos")
    return render_template("login.html")



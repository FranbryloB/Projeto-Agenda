from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import SessionLocal
from models.usuario_model import Usuario

usuario_bp = Blueprint("usuario", __name__)

@usuario_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")

        db = SessionLocal()
        existing = db.query(Usuario).filter_by(email=email).first()
        if existing:
            db.close()
            flash("Email já cadastrado.", "error")
            return render_template("register_user.html")
        novo = Usuario(nome=nome, email=email, senha=generate_password_hash(senha))
        db.add(novo)
        db.commit()
        db.close()

        flash("Cadastro realizado com sucesso. Faça login.", "success")
        return redirect(url_for("usuario.login"))

    return render_template("register_user.html")


@usuario_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("senha")

        db = SessionLocal()
        usuario = db.query(Usuario).filter_by(email=email).first()
        db.close()

        if usuario:
            session["usuario_id"] = usuario.id
            session["usuario_nome"] = usuario.nome
            return redirect(url_for("index"))

        if not check_password_hash(usuario.senha, senha):
            flash("Senha incorreta.", "error")
            return render_template("login.html")
            
        flash("Usuário ou senha incorretos.", "error")
        return render_template("login.html")

    return render_template("login.html")


@usuario_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("usuario.login"))

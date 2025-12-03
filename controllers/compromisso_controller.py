from flask import Blueprint, render_template, request, redirect, url_for, session, abort, flash
from database.db import SessionLocal
from models.compromisso_model import Compromisso

compromisso_bp = Blueprint("compromisso", __name__)

def _require_login():
    if "usuario_id" not in session:
        return False
    return True

@compromisso_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if not _require_login():
        return redirect(url_for("usuario.login"))

    if request.method == "POST":
        titulo = request.form.get("titulo")
        data = request.form.get("data")
        hora = request.form.get("hora")
        descricao = request.form.get("descricao")

        db = SessionLocal()
        novo = Compromisso(
            titulo=titulo,
            data=data,
            hora=hora,
            descricao=descricao,
            usuario_id=session["usuario_id"]
        )
        db.add(novo)
        db.commit()
        db.close()

        return redirect(url_for("compromisso.listar"))

    return render_template("cadastro.html")


@compromisso_bp.route("/listar")
def listar():
    if not _require_login():
        return redirect(url_for("usuario.login"))

    db = SessionLocal()
    compromissos = db.query(Compromisso).filter_by(usuario_id=session["usuario_id"]).all()
    db.close()
    return render_template("listar.html", compromissos=compromissos)


@compromisso_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if not _require_login():
        return redirect(url_for("usuario.login"))

    db = SessionLocal()
    compromisso = db.query(Compromisso).filter_by(id=id, usuario_id=session["usuario_id"]).first()
    if not compromisso:
        db.close()
        abort(403)  # não autorizado

    if request.method == "POST":
        compromisso.titulo = request.form.get("titulo")
        compromisso.data = request.form.get("data")
        compromisso.hora = request.form.get("hora")
        compromisso.descricao = request.form.get("descricao")
        db.commit()
        db.close()
        return redirect(url_for("compromisso.listar"))

    db.close()
    return render_template("editar.html", compromisso=compromisso)


@compromisso_bp.route("/excluir/<int:id>")
def excluir(id):
    if not _require_login():
        return redirect(url_for("usuario.login"))

    db = SessionLocal()
    compromisso = db.query(Compromisso).filter_by(id=id, usuario_id=session["usuario_id"]).first()
    if compromisso:
        db.delete(compromisso)
        db.commit()
    db.close()
    return redirect(url_for("compromisso.listar"))


@compromisso_bp.route("/concluir/<int:id>")
def concluir(id):
    if not _require_login():
        return redirect(url_for("usuario.login"))

    db = SessionLocal()
    compromisso = db.query(Compromisso).filter_by(id=id, usuario_id=session["usuario_id"]).first()
    if compromisso:
        compromisso.concluido = True
        db.commit()
    db.close()
    return redirect(url_for("compromisso.listar"))


@compromisso_bp.route("/desfazer/<int:id>")
def desfazer(id):
    if not _require_login():
        return redirect(url_for("usuario.login"))

    db = SessionLocal()
    compromisso = db.query(Compromisso).filter_by(id=id, usuario_id=session["usuario_id"]).first()
    if compromisso:
        compromisso.concluido = False
        db.commit()
    db.close()
    return redirect(url_for("compromisso.listar"))

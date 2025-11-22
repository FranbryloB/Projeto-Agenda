from flask import Flask, render_template, request, redirect, url_for
from models.compromisso_model import (
    adicionar_compromisso, listar_compromissos, buscar_compromisso,
    editar_compromisso, excluir_compromisso, marcar_concluido, desmarcar_concluido
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        adicionar_compromisso(
            request.form['titulo'],
            request.form['data'],
            request.form['hora'],
            request.form['descricao']
        )
        return redirect(url_for('listar'))

    return render_template('cadastro.html')

@app.route('/listar')
def listar():
    compromissos = listar_compromissos()
    return render_template('listar.html', compromissos=compromissos)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    compromisso = buscar_compromisso(id)

    if request.method == 'POST':
        editar_compromisso(
            id,
            request.form['titulo'],
            request.form['data'],
            request.form['hora'],
            request.form['descricao']
        )
        return redirect(url_for('listar'))

    return render_template('editar.html', compromisso=compromisso)

@app.route('/excluir/<int:id>')
def excluir(id):
    excluir_compromisso(id)
    return redirect(url_for('listar'))

@app.route('/concluir/<int:id>')
def concluir(id):
    marcar_concluido(id)
    return redirect(url_for('listar'))

@app.route('/desfazer/<int:id>')
def desfazer(id):
    desmarcar_concluido(id)
    return redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(debug=True)

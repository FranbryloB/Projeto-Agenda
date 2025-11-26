from flask import Flask, render_template, request, redirect, url_for, session
from models.compromisso_model import ( adicionar_compromisso, listar_compromissos, buscar_compromisso, editar_compromisso, excluir_compromisso, marcar_concluido, desmarcar_concluido)
from models.usuario_model import (criar_tabela_usuarios, cadastrar_usuario, buscar_usuario_por_email)

app = Flask(__name__)
app.secret_key = "uma_chave_muito_segura"
criar_tabela_usuarios()  

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
    if 'usuario_id' not in session:
        return redirect(url_for('login'))
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        cadastrar_usuario(nome, email, senha)

        return redirect(url_for('login'))

    return render_template('register_user.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = buscar_usuario_por_email(email)

        if usuario and usuario[3] == senha:
            session['usuario_id'] = usuario[0]
            session['usuario_nome'] = usuario[1]
            return redirect(url_for('index'))

        return "Usuário ou senha incorretos."

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

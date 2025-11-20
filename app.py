from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

compromissos = []

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        data = request.form['data']
        hora = request.form['hora']
        descricao = request.form['descricao']

        compromisso = {
            'titulo': titulo,
            'data': data,
            'hora': hora,
            'descricao': descricao
        }

        compromissos.append(compromisso)

        return redirect(url_for('listar'))

    return render_template('cadastrar.html')

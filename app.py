from flask import Flask, render_template
from database.db import Base, engine
import models  # garante que os modelos sejam registrados no metadata

from controllers.usuario_controller import usuario_bp
from controllers.compromisso_controller import compromisso_bp

app = Flask(__name__)
app.secret_key = "uma_chave_muito_segura"

app.register_blueprint(usuario_bp)
app.register_blueprint(compromisso_bp)

Base.metadata.create_all(bind=engine)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

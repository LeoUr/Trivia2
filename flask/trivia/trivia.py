from flask import Flask, render_template
from trv_functions import db

app = Flask(__name__)
# modo para desarrollo
app.run(debug=True)
# clave para ofuscar las cookies. Relativo a la identificación de sesiones
app.secret_key = b'^S&.+`VuXa7#\gS*'

@app.route('/')
def inicio():
    return render_template('baseLayout.html.j2')


@app.route('/categorias')
def listar_categorias():
    categorias = ""
    valores = db.consultar()

    for c in valores:
        categorias += '<a class="anchor_boton" href="/cat/' + c[0] + '">' + c[0] + '</a>'
    return render_template('categorias.html.j2', lista_categorias=categorias)


@app.route('/cat/<categoria>')
def categoria(categoria):
        return categoria


if __name__=='__main__':
    # para forzar el localhost y el puerto HTTP
    app.run('127.0.0.1', 80)

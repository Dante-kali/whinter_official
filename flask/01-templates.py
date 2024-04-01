from flask import Flask, request, render_template_string
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('xx.html')

app = Flask("Mi servidor")

@app.route("/")
def welcome():
    return '''<h1> Bienvenido a Mi servidor</h1>
    <h3>Rutas Posibles:</h3>
    <li>/seleccion</li>'''

@app.route("/seleccion")
def views():
    selection = {
        "players" : [
            "Emiliano Martínez - Arquero",
        "Nicolás Otamendi - Defensor",
        "Nahuel Molina - Defensor",
        "Gonzalo Montiel - Defensor",
        "Lisandro Martínez - Defensor",
        "Giovani Lo Celso - Mediocampista",
        "Rodrigo De Paul - Mediocampista",
        "Leandro Paredes - Mediocampista",
        "Lionel Messi - Delantero",
        "Lautaro Martínez - Delantero",
        "Ángel Di María - Delantero"
       ]
    }
    rendered_template = template.render(selection)
    return rendered_template

app.run(debug=True, port=8000)
from flask import Flask, request, render_template_string
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('yy.html')

env2 = Environment(loader=FileSystemLoader('.'))
template2 = env2.get_template('ww.html')

app = Flask("My server")

@app.route("/")
def welcome():
    data = {
        'parts' : [
        {'title' : 'Welcome to the server'},
        {'subtitle' : 'Path available'},
        {'path' : '/selection'}
        ]
        }
    rendered_template2 = template2.render(data)
    return rendered_template2


@app.route("/selection")
def mi_vista():
    contexto_dict = {
        'players': [
            {"nombre": "Emiliano Martínez ", "rol": "arquero"},
            {"nombre": "Nicolas Otamendi ", "rol": "defensor"},
            {"nombre": "Nahuel Molina ", "rol": "defensor"},
            {"nombre": "Gonzalo Montiel ", "rol": "defensor"},
            {"nombre": "Lisando Martinez ", "rol": "defensor"},
            {"nombre": "Angel di maria", "rol": "mediocampista"},
            {"nombre": "Julián Álvarez", "rol": "delantero"},
        ]
    }
    rendered_template = template.render(contexto_dict)
    return rendered_template

app.run(debug=True, port=8000)
from flask import Flask, request, render_template_string
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('xx.html')

env2 = Environment(loader=FileSystemLoader('.'))
template2 = env2.get_template('zz.html')

app = Flask("My server")

@app.route("/")
def welcome():
    data = {
        'title' : 'Welcome to the server',
        'subtitle' : 'Path available',
        'path' : '/selection'
    }
    rendered_template2 = template2.render(data)
    print(rendered_template2)
    return rendered_template2

@app.route("/selection")
def views():
    selection = {
        'players': [
            "Emiliano Martínez - Arquero",
            "Nicolas Otamendi - Defensor",
            "Nahuel Molina - Defensor",
            "Gonzalo Montiel - Defensor",
            "Lisando Martinez - Defensor",
            "Angel di maria - Mediocampista"
        ]
    }
    rendered_template = template.render(selection)
    print(rendered_template)
    return rendered_template

app.run(debug=True, port=8080)
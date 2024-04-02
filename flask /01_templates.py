from flask import Flask, request, render_template_string
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('xx.html')


app = Flask("My server")

@app.route("/seleccion")
def mi_vista():
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

app.run(debug=True, port=8000)
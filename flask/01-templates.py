from flask import Flask, request, render_template_string
from jinja2 import Environment, FileSystemLoader

app = Flask("Mi servidor")

@app.route("/seleccion")
def views():
    players = {
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
    
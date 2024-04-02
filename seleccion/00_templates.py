from flask import Flask


app = Flask("My server")

@app.route("/")
def saludo():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My server</title>
    </head>
    <body>
        <h1>Welcome to the server</h1>
        <h3><p>Available Path: </h3> 
        <a href="/selection">/selection</a></p>
    </body>
    </html>"""

@app.route("/selection")
def seleccion():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>the selection national</title>
    </head>
    <body>
        <h1>These are the 11 starting players</h1>
        <ul>
            <li>Emiliano Martínez - Arquero</li>
            <li>Nicolas Otamendi - Defensor</li>
            <li>Nahuel Molina - Defensor</li>
            <li>Gonzalo Montiel - Defensor</li>
            <li>Lisando Martinez - Defensor</li>
            <li>Enzo Perez - Mediocampista</li>
            <li>Rodrigo De Paul - Mediocampista</li>
            <li>Alexis McAllister - Mediocampista</li>
            <li>Julián Álvarez - Delantero</li>
            <li>Ángel Di María - Delantero</li>
            <li>Lionel Messi - Delantero</li>
        </ul>
    </body>
    </html>
    """


app.run(debug=True, port=8000)
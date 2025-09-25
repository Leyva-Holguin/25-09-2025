from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    mensaje = "<h1>Suma, resta, dividir, multiplicar, minino, maximo los numeros 10 y 20</h1>"
    
    mensaje += "<ul>"
    mensaje += "<li><h2>Suma http://127.0.0.1:5000/suma/10/20</h2></li>"
    mensaje += "<li><h2>resta http://127.0.0.1:5000/resta/10/20</h2></li>"
    mensaje += "<li><h2>multiplicacion http://127.0.0.1:5000/multiplicacion/10/20</h2></li>"
    mensaje += "<li><h2>division http://127.0.0.1:5000/division/10/20</h2></li>"
    mensaje += "<li><h2>minimo http://127.0.0.1:5000/minimo/10/20</h2></li>"
    mensaje += "<li><h2>maximo http://127.0.0.1:5000/maximo/10/20</h2></li>"    
    mensaje += "</ul>"
    return mensaje

@app.route("/suma/<v1>/<v2>")
def sumar(v1, v2):
    s = float(v1) + float(v2)
    return "<h1> La suma de " + str(v1) + " y " + str(v2) + " es " + str(s) + "</h1>"

@app.route("/resta/<v1>/<v2>")
def restar(v1, v2):
    s = float(v1) - float(v2)
    return "<h1> La resta de " + str(v1) + " y " + str(v2) + " es " + str(s) + "</h1>"

@app.route("/multiplicacion/<v1>/<v2>")
def multi(v1, v2):
    return

@app.route("/division/<v1>/<v2>")
def div(v1, v2):
    return

@app.route("/minimo/<v1>/<v2>")
def min(v1, v2):
    return

@app.route("/maximo/<v1>/<v2>")
def max(v1, v2):
    return

if __name__ == '__main__':
    app.run(debug=True)
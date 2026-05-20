from flask import Flask
from flask import render_template
#crear una instacia de flask que sera nuestra aplicacion 
app = Flask(__name__)

#por cada ruta que vayamos a atender en el navegador cramos una funcion en pyton.

@app.route("/") #el decorrador indica la ruta que llama a esta funcion

def hola():
    #lo que la funcion retorne, llega en el cuerpo HTML al navegador
    return  """<p>HOLA</>"""
@app.route("/biografia")
def biografia():
    return render_template("hola.html")


#iniciar la aplicacion flask
app.run(debug=True)



import sys
sys.path.append("src")

from flask import Flask
from flask import render_template, request
from model.logica_calculohipoteca_comentado import credito, calculadora_hipoteca_inversa
from controller.calculos_controller import CalculosController

from view.web import vista_calculos

app = Flask(__name__)


app.register_blueprint(vista_calculos.blueprint)


if __name__ == '__main__':
    app.run(debug=True)



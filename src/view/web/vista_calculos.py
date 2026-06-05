import sys
sys.path.append("src")

from flask import Blueprint
from flask import render_template, request
from model.logica_calculohipoteca_comentado import credito, calculadora_hipoteca_inversa
from controller.calculos_controller import CalculosController

blueprint = Blueprint("Vista_calculos",__name__, "templates")



@blueprint.route('/')
def datos():
    return render_template('datos.html')
@blueprint.route('/crear_tabla')
def crear_tabla():
    CalculosController.crear_tabla()
    return "Tabla creada"



@blueprint.route('/guardar_calculos')
def guardar_calculos():
    datos = credito(cedula = str(request.args["cedula"]),valor_inmueble=int(request.args["valor_inmueble"]), tasa_capitalizacion=float(request.args["tasa_capitalizacion"]), 
                    plazo_simulacion=int(request.args["plazo_simulacion"]), porcentaje_LTV=float(request.args["porcentaje_LTV"]), 
                    edad=int(request.args["edad"]))
    monto_mensual_recibido = f"{calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(datos):.0f}"
    total_recibido_acumulado = f"{calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(datos):.0f}"
    saldo_proyectado = f"{calculadora_hipoteca_inversa.calcular_saldo_proyectado(datos):.0f}"
    CalculosController.insertar(datos)
    return render_template('cuotas.html', cedula = datos.cedula, valor_inmueble=datos.valor_inmueble,
                            tasa_capitalizacion=datos.tasa_capitalizacion, plazo_simulacion=datos.plazo_simulacion,
                              porcentaje_LTV=datos.porcentaje_LTV, edad=datos.edad, monto_mensual_recibido=monto_mensual_recibido, 
                              total_recibido_acumulado=total_recibido_acumulado, saldo_proyectado=saldo_proyectado)

if __name__ == '__main__':
    blueprint.run(debug=True)


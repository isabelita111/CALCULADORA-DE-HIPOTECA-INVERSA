from flask import Flask
from flask import render_template, request
from src.model.logica_calculohipoteca_comentado import credito, calculadora_hipoteca_inversa

app = Flask(__name__)



@app.route('/datos')
def datos():
    return render_template('datos.html')

@app.route('/calcular_montos')
def cuotas():
    datos = credito(valor_inmueble=int(request.args["valor_inmueble"]), tasa_capitalizacion=float(request.args["tasa_capitalizacion"]), 
                    plazo_simulacion=int(request.args["plazo_simulacion"]), porcentaje_LTV=float(request.args["porcentaje_LTV"]), 
                    edad=int(request.args["edad"]))
    monto_mensual_recibido = f"{calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(datos):.0f}"
    total_recibido_acumulado = f"{calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(datos):.0f}"
    saldo_proyectado = f"{calculadora_hipoteca_inversa.calcular_saldo_proyectado(datos):.0f}"
    return render_template('cuotas.html', valor_inmueble=datos.valor_inmueble, tasa_capitalizacion=datos.tasa_capitalizacion, plazo_simulacion=datos.plazo_simulacion, porcentaje_LTV=datos.porcentaje_LTV, edad=datos.edad, monto_mensual_recibido=monto_mensual_recibido, total_recibido_acumulado=total_recibido_acumulado, saldo_proyectado=saldo_proyectado)

if __name__ == '__main__':
    app.run(debug=True)



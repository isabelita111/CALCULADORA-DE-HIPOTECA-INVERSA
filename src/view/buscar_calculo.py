import sys
sys.path.append("src")

from model.calculos import Calculo
from controller.calculos_controller import calculosController

try:
    cedula = input("Ingrese la cédula del cálculo que desea buscar: ")
    calculo_buscado = calculosController.buscar_cedula(cedula)

    print(f"\nCálculo encontrado:")
    print(f"  Cédula                   : {calculo_buscado.cedula}")
    print(f"  Valor del inmueble       : ${calculo_buscado.valor_inmueble:,.0f}")
    print(f"  Tasa capitalización      : {calculo_buscado.tasa_capitalizacion * 100:.2f}%")
    print(f"  Edad                     : {calculo_buscado.edad} años")
    print(f"  Plazo simulación         : {calculo_buscado.plazo_simulacion} años")
    print(f"  Porcentaje LTV           : {calculo_buscado.porcentaje_LTV * 100:.0f}%")
    print(f"  Monto mensual recibido   : ${calculo_buscado.monto_mensual_recibido:,.0f}")
    print(f"  Total recibido acumulado : ${calculo_buscado.total_recibido_acumulado:,.0f}")
    print(f"  Saldo proyectado         : ${calculo_buscado.saldo_proyectado:,.0f}")

except Exception as err:
    print("Error:")
    print(str(err))
 
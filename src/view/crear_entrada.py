import sys
sys.path.append("src")

from model.calculos import Calculo
from controller.calculos_controller import calculosController

print("Por favor ingrese los datos para calcular la hipoteca inversa")

cedula              = input("Cédula: ")
valor_inmueble      = float(input("Valor del inmueble: "))
tasa_capitalizacion = float(input("Tasa de capitalización (ej: 0.08 para 8%): "))
edad                = int(input("Edad: "))
plazo_simulacion    = int(input("Plazo de simulación (años): "))
porcentaje_LTV      = float(input("Porcentaje LTV permitido (ej: 0.70 para 70%): "))

calculo = Calculo(
    cedula=cedula,
    valor_inmueble=valor_inmueble,
    tasa_capitalizacion=tasa_capitalizacion,
    edad=edad,
    plazo_simulacion=plazo_simulacion,
    porcentaje_LTV=porcentaje_LTV,
    monto_mensual_recibido=0,
    total_recibido_acumulado=0,
    saldo_proyectado=0
)

calculosController.insertar(calculo)

# Mostrar los resultados calculados
resultado = calculosController.buscar_cedula(cedula)
print("\n¡Cálculo registrado correctamente!")
print(f"\nResultados:")
print(f"  Monto mensual recibido   : ${resultado.monto_mensual_recibido:,.0f}")
print(f"  Total recibido acumulado : ${resultado.total_recibido_acumulado:,.0f}")
print(f"  Saldo proyectado         : ${resultado.saldo_proyectado:,.0f}")
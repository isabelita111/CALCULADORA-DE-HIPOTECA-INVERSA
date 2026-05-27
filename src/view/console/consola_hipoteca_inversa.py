import sys
sys.path.append("src")
from model.logica_calculohipoteca_comentado import credito, calculadora_hipoteca_inversa


from model import logica_calculohipoteca_comentado
from model.logica_calculohipoteca_comentado import credito



valor_inmueble = int(input("Ingrese el valor del inmueble: "))

tasa_capitalizacion = float(input("ingrese la tasa de capitalizacion del banco: "))

plazo_simulacion = int(input("ingrese el plazo de simulacion:"))

porcentaje_LTV = float(input(" ingrese el porcentaje LTV permitido: "))

edad = int(input("Ingrese su edad: "))
datos = credito(valor_inmueble, tasa_capitalizacion, plazo_simulacion, porcentaje_LTV, edad)
monto_mensual_recibido = logica_calculohipoteca_comentado.calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(datos)
Total_recibido_acumulado = logica_calculohipoteca_comentado.calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(datos)
saldo_proyectado = logica_calculohipoteca_comentado.calculadora_hipoteca_inversa.calcular_saldo_proyectado(datos)

print(f"La cuota mensual es de: ${monto_mensual_recibido:.0f}")
print(f"El total acumulado es de: ${Total_recibido_acumulado:.0f}")
print(f"El saldo proyectado es de: ${saldo_proyectado:.0f}")





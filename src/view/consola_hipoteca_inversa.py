from src.model import logica_calculohipoteca_comentado




import logica_calculohipoteca_comentado
import test_calculadora_hipoteca_comentado


valor_inmueble = int(input("Ingrese el valor del inmueble: "))

tasa_capitalizacion = float(input("ingrese la tasa de capitalizacion del banco: "))

plazo_simulacion = int(input("ingrese el plazo de simulacion:"))

porcentaje_LTV = float(input(" ingrese el porcentaje LTV permitido: "))

edad = int(input("Ingrese su edad: "))

monto_mensual_recibido, Total_recibido_acumulado, saldo_proyectado = logica_calculohipoteca_comentado.calcular_credito(
    valor_inmueble, tasa_capitalizacion, plazo_simulacion, porcentaje_LTV, edad
)

print(f"La cuota mensual es de: ${monto_mensual_recibido:.0f}")
print(f"El total acumulado es de: ${Total_recibido_acumulado:.0f}")
print(f"El saldo proyectado es de: ${saldo_proyectado:.0f}")



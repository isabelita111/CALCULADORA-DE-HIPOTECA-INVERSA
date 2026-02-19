import logica_calculohipoteca
import calculadora_hipoteca


valor_inmueble = int(input("Ingrese el valor del inmueble: "))

tasa_anual = float(input("ingrese la tasa anual del banco: "))

plazo_anios = int(input("ingrese el plazo:"))

porcentaje_financiado = float(input(" ingrese el porcentaje financiado: "))

edad = int(input("Ingrese su edad: "))

cuota_mensual, total_acumulado, saldo_proyectado = logica_calculohipoteca.calcular_credito(
    valor_inmueble, tasa_anual, plazo_anios, porcentaje_financiado, edad
)

print(f"La cuota mensual es de: ${cuota_mensual:.0f}")
print(f"El total acumulado es de: ${total_acumulado:.0f}")
print(f"El saldo proyectado es de: ${saldo_proyectado:.0f}")



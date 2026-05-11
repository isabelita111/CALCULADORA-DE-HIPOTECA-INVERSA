import sys
sys.path.append("src")
 
from model.entradas import Entrada
from controller.entradas_controller import EntradasController
 
 
# Crear una entrada vacía
entrada = Entrada(cedula="", valor_inmueble=0, tasa_capitalizacion=0,
                  edad=0, plazo_simulacion=0, porcentaje_LTV=0)
 
print("Por favor ingrese los datos para calcular la hipoteca inversa")
 
entrada.cedula              = input("Cédula: ")
entrada.valor_inmueble      = float(input("Valor del inmueble: "))
entrada.tasa_capitalizacion = float(input("Tasa de capitalización (ej: 0.08 para 8%): "))
entrada.edad                = int(input("Edad: "))
entrada.plazo_simulacion    = int(input("Plazo de simulación (años): "))
entrada.porcentaje_LTV      = float(input("Porcentaje LTV permitido (ej: 0.70 para 70%): "))
 
EntradasController.insertar(entrada)
 
print("¡Entrada registrada correctamente!")
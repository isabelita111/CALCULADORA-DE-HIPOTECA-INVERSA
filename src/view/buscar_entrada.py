import sys
sys.path.append("src")
 
from model.entradas import Entrada
from controller.entradas_controller import EntradasController
 
try:
    cedula = input("Ingrese la cédula de la entrada que desea buscar: ")
    entrada_buscada = EntradasController.buscar_cedula(cedula)
 
    print(f"\nEntrada encontrada:")
    print(f"  Cédula              : {entrada_buscada.cedula}")
    print(f"  Valor del inmueble  : ${entrada_buscada.valor_inmueble:,.0f}")
    print(f"  Tasa capitalización : {entrada_buscada.tasa_capitalizacion * 100:.2f}%")
    print(f"  Edad                : {entrada_buscada.edad} años")
    print(f"  Plazo simulación    : {entrada_buscada.plazo_simulacion} años")
    print(f"  Porcentaje LTV      : {entrada_buscada.porcentaje_LTV * 100:.0f}%")
 
except Exception as err:
    print("Error:")
    print(str(err))
 
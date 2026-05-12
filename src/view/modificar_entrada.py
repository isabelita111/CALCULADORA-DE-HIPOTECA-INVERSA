import sys
sys.path.append("src")
 
from model.entradas import Entrada
from controller.entradas_controller import EntradasController
 
try:
    cedula = input("Ingrese la cédula de la entrada que desea modificar: ")
 
    # Verificar que existe antes de modificar
    entrada_actual = EntradasController.buscar_cedula(cedula)
 
    print(f"\nEntrada actual:")
    print(f"  Valor del inmueble  : ${entrada_actual.valor_inmueble:,.0f}")
    print(f"  Tasa capitalización : {entrada_actual.tasa_capitalizacion * 100:.2f}%")
    print(f"  Edad                : {entrada_actual.edad} años")
    print(f"  Plazo simulación    : {entrada_actual.plazo_simulacion} años")
    print(f"  Porcentaje LTV      : {entrada_actual.porcentaje_LTV * 100:.0f}%")
 
    print("\n¿Qué desea hacer?")
    print("  1. Actualizar datos")
    print("  2. Eliminar entrada")
    opcion = input("\nOpción: ")
 
    if opcion == "1":
        print("\nIngrese los nuevos datos (Enter para conservar el valor actual):")
 
        valor = input(f"Valor del inmueble [{entrada_actual.valor_inmueble:,.0f}]: ")
        tasa  = input(f"Tasa de capitalización [{entrada_actual.tasa_capitalizacion}]: ")
        edad  = input(f"Edad [{entrada_actual.edad}]: ")
        plazo = input(f"Plazo de simulación [{entrada_actual.plazo_simulacion}]: ")
        ltv   = input(f"Porcentaje LTV [{entrada_actual.porcentaje_LTV}]: ")
 
        entrada_actualizada = Entrada(
            cedula              = cedula,
            valor_inmueble      = float(valor) if valor else entrada_actual.valor_inmueble,
            tasa_capitalizacion = float(tasa)  if tasa  else entrada_actual.tasa_capitalizacion,
            edad                = int(edad)    if edad  else entrada_actual.edad,
            plazo_simulacion    = int(plazo)   if plazo else entrada_actual.plazo_simulacion,
            porcentaje_LTV      = float(ltv)   if ltv   else entrada_actual.porcentaje_LTV
        )
 
        EntradasController.actualizar(entrada_actualizada)
        print("\n¡Entrada actualizada correctamente!")
 
    elif opcion == "2":
        confirmar = input(f"\n¿Está seguro que desea eliminar la entrada con cédula {cedula}? (s/n): ")
        if confirmar.lower() == "s":
            EntradasController.eliminar(cedula)
            print("¡Entrada eliminada correctamente!")
        else:
            print("Operación cancelada.")
 
    else:
        print("Opción no válida.")
 
except Exception as err:
    print("Error:")
    print(str(err))
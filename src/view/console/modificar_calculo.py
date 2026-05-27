import sys
sys.path.append("src")
 
from model.calculos import Calculo
from controller.calculos_controller import calculosController
 
try:
    cedula = input("Ingrese la cédula del cálculo que desea modificar: ")
 
    # Verificar que existe antes de modificar
    calculo_actual = calculosController.buscar_cedula(cedula)
 
    print(f"\nDatos actuales:")
    print(f"  Valor del inmueble       : ${calculo_actual.valor_inmueble:,.0f}")
    print(f"  Tasa capitalización      : {calculo_actual.tasa_capitalizacion * 100:.2f}%")
    print(f"  Edad                     : {calculo_actual.edad} años")
    print(f"  Plazo simulación         : {calculo_actual.plazo_simulacion} años")
    print(f"  Porcentaje LTV           : {calculo_actual.porcentaje_LTV * 100:.0f}%")
    print(f"  Monto mensual recibido   : ${calculo_actual.monto_mensual_recibido:,.0f}")
    print(f"  Total recibido acumulado : ${calculo_actual.total_recibido_acumulado:,.0f}")
    print(f"  Saldo proyectado         : ${calculo_actual.saldo_proyectado:,.0f}")
 
    print("\n¿Qué desea hacer?")
    print("  1. Actualizar datos")
    print("  2. Eliminar cálculo")
    opcion = input("\nOpción: ")
 
    if opcion == "1":
        print("\nIngrese los nuevos datos (Enter para conservar el valor actual):")
 
        valor = input(f"Valor del inmueble [{calculo_actual.valor_inmueble:,.0f}]: ")
        tasa  = input(f"Tasa de capitalización [{calculo_actual.tasa_capitalizacion}]: ")
        edad  = input(f"Edad [{calculo_actual.edad}]: ")
        plazo = input(f"Plazo de simulación [{calculo_actual.plazo_simulacion}]: ")
        ltv   = input(f"Porcentaje LTV [{calculo_actual.porcentaje_LTV}]: ")
 
        calculo_actualizado = Calculo(
            cedula                   = cedula,
            valor_inmueble           = float(valor) if valor else calculo_actual.valor_inmueble,
            tasa_capitalizacion      = float(tasa)  if tasa  else calculo_actual.tasa_capitalizacion,
            edad                     = int(edad)    if edad  else calculo_actual.edad,
            plazo_simulacion         = int(plazo)   if plazo else calculo_actual.plazo_simulacion,
            porcentaje_LTV           = float(ltv)   if ltv   else calculo_actual.porcentaje_LTV,
            monto_mensual_recibido   = 0,
            total_recibido_acumulado = 0,
            saldo_proyectado         = 0
        )
 
        calculosController.actualizar(calculo_actualizado)
 
        # Mostrar los nuevos resultados recalculados
        calculo_nuevo = calculosController.buscar_cedula(cedula)
        print("\n¡Cálculo actualizado correctamente!")
        print(f"\nNuevos resultados:")
        print(f"  Monto mensual recibido   : ${calculo_nuevo.monto_mensual_recibido:,.0f}")
        print(f"  Total recibido acumulado : ${calculo_nuevo.total_recibido_acumulado:,.0f}")
        print(f"  Saldo proyectado         : ${calculo_nuevo.saldo_proyectado:,.0f}")
 
    elif opcion == "2":
        confirmar = input(f"\n¿Está seguro que desea eliminar el cálculo con cédula {cedula}? (s/n): ")
        if confirmar.lower() == "s":
            calculosController.eliminar(cedula)
            print("¡Cálculo eliminado correctamente!")
        else:
            print("Operación cancelada.")
 
    else:
        print("Opción no válida.")
 
except Exception as err:
    print("Error:")
    print(str(err))
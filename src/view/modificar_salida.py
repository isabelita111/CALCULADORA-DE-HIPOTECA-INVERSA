import sys
sys.path.append("..")
 
from src.model.salidas import Salidas
from controller.salidas_controller import SalidasController
 
try:
    id_calculo = input("Ingrese el ID del cálculo que desea modificar: ")
 
    # Verificar que existe antes de modificar
    salida_actual = SalidasController.buscar_salidas(id_calculo)
 
    print(f"\nSalida actual:")
    print(f"  Monto mensual recibido   : ${salida_actual.monto_mensual_recibido:,.0f}")
    print(f"  Total recibido acumulado : ${salida_actual.total_recibido_acumulado:,.0f}")
    print(f"  Saldo proyectado         : ${salida_actual.saldo_proyectado:,.0f}")
 
    print("\n¿Qué desea hacer?")
    print("  1. Actualizar datos")
    print("  2. Eliminar salida")
    opcion = input("\nOpción: ")
 
    if opcion == "1":
        print("\nIngrese los nuevos datos (Enter para conservar el valor actual):")
 
        monto = input(f"Monto mensual recibido [{salida_actual.monto_mensual_recibido:,.0f}]: ")
        total = input(f"Total recibido acumulado [{salida_actual.total_recibido_acumulado:,.0f}]: ")
        saldo = input(f"Saldo proyectado [{salida_actual.saldo_proyectado:,.0f}]: ")
 
        salida_actualizada = Salidas(
            id_calculo               = id_calculo,
            monto_mensual_recibido   = float(monto) if monto else salida_actual.monto_mensual_recibido,
            total_recibido_acumulado = float(total) if total else salida_actual.total_recibido_acumulado,
            saldo_proyectado         = float(saldo) if saldo else salida_actual.saldo_proyectado
        )
 
        SalidasController.actualizar(salida_actualizada)
        print("\n¡Salida actualizada correctamente!")
 
    elif opcion == "2":
        confirmar = input(f"\n¿Está seguro que desea eliminar el cálculo {id_calculo}? (s/n): ")
        if confirmar.lower() == "s":
            SalidasController.eliminar(id_calculo)
            print("¡Salida eliminada correctamente!")
        else:
            print("Operación cancelada.")
 
    else:
        print("Opción no válida.")
 
except Exception as err:
    print("Error:")
    print(str(err))
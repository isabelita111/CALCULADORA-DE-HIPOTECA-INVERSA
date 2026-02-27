class Error_edad(Exception):
    "se usa cuando la edad es menor a la edad minima para solicitar la hipoteca inversa"
class Eror_porcentaje(Exception):
    "la edad mínima para solicitar hipoteca inversa es de 62 años."

class Error_tasa_negativa(Exception):
    "Error: la tasa de interés debe ser mayor a 0."

def calcular_credito(valor_inmueble, tasa_capitalizacion, plazo_simulacion, porcentaje_LTV, edad):
    """
    Calcula los valores principales de una hipoteca inversa:
    - Cuota mensual
    - Total acumulado pagado
    - Saldo proyectado al final del plazo
    """

    # VALIDACIONES: Se verifican las condiciones mínimas para que el crédito sea válido.
    if edad < 62:
        raise Error_edad ("Error: la edad mínima para solicitar hipoteca inversa es de 65 años.")
    
    # Se valida que el porcentaje financiado esté dentro del rango permitido (0% a 100%).
    if porcentaje_LTV < 0 or porcentaje_LTV > 100:
        raise Eror_porcentaje ("Error: el porcentaje financiado debe ser entre 0 y 100.")
    
    # Se valida que la tasa de interés sea positiva.
    if tasa_capitalizacion <= 0:
        raise Error_tasa_negativa ("Error: la tasa de interés debe ser mayor a 0.")


    # CONVERSIÓN A DECIMALES: Se transforman porcentajes a formato decimal para operar matemáticamente.
    tasa_capitalizacion = tasa_capitalizacion / 100
    porcentaje_LTV = porcentaje_LTV / 100


    # CÁLCULOS PRINCIPALES
    
    # Se calcula el monto real que será financiado según el porcentaje indicado.
    monto_financiado = valor_inmueble * porcentaje_LTV
    
    # Se convierte la tasa anual en tasa mensual.
    tasa_mensual = tasa_capitalizacion / 12
    
    # Se calcula el número total de pagos en meses.
    numero_pagos = plazo_simulacion * 12


    # CUOTA MENSUAL:
    # Se aplica la fórmula financiera de anualidad (equivalente a la función PAGO de Excel).
    monto_mensual_recibido = (
        tasa_mensual * monto_financiado
        / (1 - (1 + tasa_mensual) ** (-numero_pagos))
    )

    
    # TOTAL ACUMULADO:
    # Se calcula el total pagado al final del crédito.
    Total_recibido_acumulado = monto_mensual_recibido * numero_pagos


    # SALDO PROYECTADO:
    # Se proyecta el valor futuro del monto financiado aplicando interés compuesto anual.
    saldo_proyectado = monto_financiado * (1 + tasa_capitalizacion) ** plazo_simulacion


    # Se retornan los tres resultados principales del cálculo.
    return monto_mensual_recibido, Total_recibido_acumulado, saldo_proyectado

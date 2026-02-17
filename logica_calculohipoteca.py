def calcular_credito(valor_inmueble, tasa_anual, plazo_anios, porcentaje_financiado, edad):

    #  VALIDACIONES 
    if edad < 65:
        return "Error: la edad mínima para solicitar hipoteca inversa es de 65 años."
    
    if porcentaje_financiado < 0 or porcentaje_financiado > 100:
        return "Error: el porcentaje financiado debe ser entre 0 y 100."
    
    if tasa_anual <= 0:
        return "Error: la tasa de interés debe ser mayor a 0."


    #  CONVERTIR A DECIMALES 
    
    tasa_anual = tasa_anual / 100
    porcentaje_financiado = porcentaje_financiado / 100


    #  CÁLCULOS 
    
    monto_financiado = valor_inmueble * porcentaje_financiado
    
    tasa_mensual = tasa_anual / 12
    numero_pagos = plazo_anios * 12


    #  CUOTA MENSUAL (equivalente a función PAGO de Excel)
    
    cuota_mensual = (
        tasa_mensual * monto_financiado
        / (1 - (1 + tasa_mensual) ** (-numero_pagos))
    )


    # TOTAL ACUMULADO
    
    total_acumulado = cuota_mensual * numero_pagos


    # SALDO PROYECTADO
    
    saldo_proyectado = monto_financiado * (1 + tasa_anual) ** plazo_anios


    return cuota_mensual, total_acumulado, saldo_proyectado


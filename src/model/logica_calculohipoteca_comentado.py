class ErrorEdad(Exception):
    """Se usa cuando la edad es menor a la edad mínima requerida."""
    pass


class ErrorPorcentaje(Exception):
    """Se usa cuando el porcentaje LTV está fuera del rango permitido (0 a 100)."""
    pass


class ErrorTasaNegativa(Exception):
    """Se usa cuando la tasa de interés es menor o igual a cero."""
    pass


class ErrorPlazo(Exception):
    """Se usa cuando el plazo de simulación es menor o igual a cero."""
    pass


def calcular_credito(valor_inmueble, tasa_capitalizacion, plazo_simulacion, porcentaje_LTV, edad):
    """
    Calcula los valores principales de una hipoteca inversa:
    - Monto mensual recibido
    - Total acumulado recibido
    - Saldo proyectado al final del plazo
    """

    # =========================
    # VALIDACIONES
    # =========================

    if edad < 62:
        raise ErrorEdad("La edad mínima para solicitar la hipoteca inversa es de 62 años.")

    if porcentaje_LTV < 0 or porcentaje_LTV > 100:
        raise ErrorPorcentaje("El porcentaje financiado debe estar entre 0 y 100.")

    if tasa_capitalizacion <= 0:
        raise ErrorTasaNegativa("La tasa de interés debe ser mayor a 0.")

    if plazo_simulacion <= 0:
        raise ErrorPlazo("El plazo de simulación debe ser mayor a 0.")

    if valor_inmueble <= 0:
        raise ValueError("El valor del inmueble debe ser mayor a 0.")

    # =========================
    # CONVERSIÓN A DECIMALES
    # =========================

    tasa_capitalizacion = tasa_capitalizacion / 100
    porcentaje_LTV = porcentaje_LTV / 100

    # =========================
    # CÁLCULOS PRINCIPALES
    # =========================

    monto_financiado = valor_inmueble * porcentaje_LTV
    tasa_mensual = tasa_capitalizacion / 12
    numero_pagos = plazo_simulacion * 12

    # Fórmula de anualidad
    monto_mensual_recibido = (
        tasa_mensual * monto_financiado
        / (1 - (1 + tasa_mensual) ** (-numero_pagos))
    )

    total_recibido_acumulado = monto_mensual_recibido * numero_pagos

    # Interés compuesto anual
    saldo_proyectado = monto_financiado * (1 + tasa_capitalizacion) ** plazo_simulacion

    return monto_mensual_recibido, total_recibido_acumulado, saldo_proyectado

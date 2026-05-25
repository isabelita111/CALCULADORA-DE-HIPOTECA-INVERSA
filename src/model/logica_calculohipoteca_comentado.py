min_edad = 65
min_LTV = 0
max_LTV = 1
min_tasa_capitalizacion = 0
min_plazo_simulacion = 0
min_valor_inmueble = 0 
 
class ErrorEdad(Exception):
    def __init__(self, edad):
        super().__init__(f"tu edad {edad} no permite solicitar la hipoteca inversa. La edad mínima para solicitar la hipoteca inversa es de {min_edad} años")
 
class ErrorPorcentaje(Exception):
    def __init__(self, porcetaje_LTV):
        super().__init__(f"El porcetaje LTV que ingresaste {porcetaje_LTV} debe estar entre {min_LTV}% y {max_LTV}% ")
 
class ErrorTasaNegativa(Exception):
    def __init__(self, tasa_capitalizacion):
        super().__init__(f"La tasa de capitalizacion {tasa_capitalizacion}debe ser mayor a {min_tasa_capitalizacion}")
 
class ErrorPlazo(Exception):
    def __init__(self, plazo_simulacion):
        super().__init__(f"El plazo que ingresaste {plazo_simulacion} debe ser mayor a {min_plazo_simulacion} ")
 
class ErrorValorInmueble(Exception):
    def __init__(self, valor_inmueble):
        super().__init__(f"Ela valor del inmueble {valor_inmueble} debe ser mayor a {min_valor_inmueble}")
 
 
class credito():
    cedula : str
    valor_inmueble : int
    tasa_capitalizacion : float
    plazo_simulacion : int
    porcentaje_LTV : float
    edad : int
 
    def __init__(self, cedula, valor_inmueble, tasa_capitalizacion, plazo_simulacion, porcentaje_LTV, edad):
        self.cedula = cedula
        self.valor_inmueble = valor_inmueble
        self.tasa_capitalizacion = tasa_capitalizacion / 100
        self.plazo_simulacion = plazo_simulacion
        self.porcentaje_LTV = porcentaje_LTV / 100
        self.edad = edad
 
class calculadora_hipoteca_inversa():   
 
    # =========================
    # VALIDACIONES
    # =========================
    def validar_edad(edad):
        """
        Args:
            edad: Edad ingresada por el usuario para solicitar la hipoteca inversa
        Raises: 
            ErrorEdad: validar si la edad es menor a la edad mínima permitida para solicitar la hipoteca inversa, si es así se lanza una excepción de tipo ErrorEdad.
        """
        if edad < min_edad:
            raise ErrorEdad(edad)
        
    def validar_porcetanje_LTV_menor_0(porcentaje_LTV):
        """
        Args:
            porcentaje_LTV: Porcentaje LTV ingresado por el usuario para solicitar la hipoteca inversa 
        Raises:
            ErrorPorcentaje: Si el porcentaje LTV ingresado es menor a 0, se lanza una excepción de tipo ErrorPorcentaje
        """
        if porcentaje_LTV < min_LTV:
            raise ErrorPorcentaje(porcentaje_LTV)
 
    def validar_porcetanje_LTV_mayor_100(porcentaje_LTV):
        """
        Args:
            porcentaje_LTV: Porcentaje LTV ingresado por el usuario para solicitar la hipoteca inversa 
        Raises:
            ErrorPorcentaje: Si el porcentaje LTV ingresado es mayor a 100, se lanza una excepción de tipo ErrorPorcentaje
        """
        if porcentaje_LTV > max_LTV:
            raise ErrorPorcentaje(porcentaje_LTV)
 
    def validar_tasa_capitalizacion(tasa_capitalizacion):
        """
        Args:
            tasa_capitalizacion : Tasa de capitalizacion ingresada por el usuario para solicitar la hipoteca inversa
        Raises:
            ErrorTasaNegativa: Si la tasa de capitalización ingresada es menor o igual a 0, se lanza una excepción de tipo ErrorTasaNegativa
        """
        if tasa_capitalizacion <= min_tasa_capitalizacion:
            raise ErrorTasaNegativa(tasa_capitalizacion)
 
    def validar_plazo_simulacion(plazo_simulacion):
        """
        Args:
            plazo_simulacion : Plazo de simulación ingresado por el usuario para solicitar la hipoteca inversa
        Raises:
            ErrorPlazo: Si el plazo de simulación ingresado es menor o igual al plazo mínimo, se lanza una excepción de tipo ErrorPlazo
        """
        if plazo_simulacion <= min_plazo_simulacion:
            raise ErrorPlazo(plazo_simulacion)
 
    def validar_valor_inmueble(valor_inmueble):
        """
        Args:
            valor_inmueble : Valor del inmueble ingresado por el usuario para solicitar la hipoteca inversa
        Raises:
            ErrorValorInmueble: Si el valor del inmueble ingresado es menor o igual al valor mínimo, se lanza una excepción de tipo ErrorValorInmueble
        """
        if valor_inmueble <= min_valor_inmueble:
            raise ErrorValorInmueble(valor_inmueble)
 
    # =========================
    # CÁLCULOS PRINCIPALES
    # =========================
 
    def calcular_monto_mensual_recibido(credito : credito):
        """
        Args:
            credito : Credito para el cual se desea calcular el monto mensual recibido
        Returns:
             _int_: El monto mensual recibido por el cliente de la hipoteca inversa, calculado utilizando la fórmula de anualidad ordinaria.
        """
        monto_financiado = credito.valor_inmueble * credito.porcentaje_LTV
        tasa_mensual = credito.tasa_capitalizacion / 12
        numero_pagos = credito.plazo_simulacion * 12
 
        monto_mensual_recibido = (tasa_mensual * monto_financiado) / (1 - (1 + tasa_mensual) ** (-numero_pagos))
        return monto_mensual_recibido
    
    def calcular_total_recibido_acumulado(credito : credito):
        """
        Args:
            credito : Credito para el cual se desea calcular el total recibido acumulado
        Returns:
            _int_: El total recibido acumulado por el cliente de la hipoteca inversa, calculado multiplicando el monto mensual recibido por el número total de pagos durante el plazo de simulación.
        """
        monto_mensual = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(credito)
        numero_pagos = credito.plazo_simulacion * 12
        total_recibido_acumulado = monto_mensual * numero_pagos
        return total_recibido_acumulado
 
    def calcular_saldo_proyectado(credito : credito):
        """
        Args:
            credito : Credito para el cual se desea calcular el saldo proyectado
        Returns:
            _int_: El saldo proyectado para el cliente de la hipoteca inversa, calculado utilizando la fórmula de interés compuesto.
        """
        monto_financiado = credito.valor_inmueble * credito.porcentaje_LTV
        saldo_proyectado = monto_financiado * (1 + credito.tasa_capitalizacion) ** credito.plazo_simulacion
        return saldo_proyectado


class Calculo:
    def __init__(self, cedula, valor_inmueble, tasa_capitalizacion, edad, plazo_simulacion, porcentaje_LTV, monto_mensual_recibido, total_recibido_acumulado, saldo_proyectado):
        self.cedula = cedula
        self.valor_inmueble = valor_inmueble
        self.tasa_capitalizacion = tasa_capitalizacion
        self.edad = edad
        self.plazo_simulacion = plazo_simulacion
        self.porcentaje_LTV = porcentaje_LTV
        self.monto_mensual_recibido = monto_mensual_recibido
        self.total_recibido_acumulado = total_recibido_acumulado
        self.saldo_proyectado = saldo_proyectado

        

    def is_equal(self, comparacion):

        assert(self.cedula == comparacion.cedula)
        assert(self.valor_inmueble == comparacion.valor_inmueble)
        assert(self.tasa_capitalizacion == comparacion.tasa_capitalizacion)
        assert(self.edad == comparacion.edad)
        assert(self.plazo_simulacion == comparacion.plazo_simulacion)
        assert(self.porcentaje_LTV == comparacion.porcentaje_LTV)
        assert(self.monto_mensual_recibido == comparacion.monto_mensual_recibido)
        assert(self.total_recibido_acumulado == comparacion.total_recibido_acumulado)
        assert(self.saldo_proyectado == comparacion.saldo_proyectado)

        return True

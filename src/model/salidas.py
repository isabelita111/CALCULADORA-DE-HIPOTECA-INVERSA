class Salidas:
    def __init__(self, id_calculo, monto_mensual_recibido, total_recibido_acumulado, saldo_proyectado):
        self.id_calculo = id_calculo
        self.monto_mensual_recibido = monto_mensual_recibido
        self.total_recibido_acumulado = total_recibido_acumulado
        self.saldo_proyectado = saldo_proyectado

    def is_equal(self, comparacion):
        assert(self.id_calculo == comparacion.id_calculo)
        assert(self.monto_mensual_recibido == comparacion.monto_mensual_recibido)
        assert(self.total_recibido_acumulado == comparacion.total_recibido_acumulado)
        assert(self.saldo_proyectado == comparacion.saldo_proyectado)

        return True
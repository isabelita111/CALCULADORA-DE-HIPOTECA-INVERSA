from datetime import date

class Entrada:
    def __init__(self, cedula, valor_inmueble, tasa_capitalizacion, edad, plazo_simulacion, porcentaje_LTV):
        self.cedula = cedula
        self.valor_inmueble = valor_inmueble
        self.tasa_capitalizacion = tasa_capitalizacion
        self.edad = edad
        self.plazo_simulacion = plazo_simulacion
        self.porcentaje_LTV = porcentaje_LTV

        

    def is_equal(self, comparacion):

        assert(self.cedula == comparacion.cedula)
        assert(self.valor_inmueble == comparacion.valor_inmueble)
        assert(self.tasa_capitalizacion == comparacion.tasa_capitalizacion)
        assert(self.edad == comparacion.edad)
        assert(self.plazo_simulacion == comparacion.plazo_simulacion)
        assert(self.porcentaje_LTV == comparacion.porcentaje_LTV)

        return True


import unittest
import logica_calculohipoteca_comentado


class TestCalculadoraHipoteca(unittest.TestCase):
    """
    Pruebas unitarias para verificar el correcto funcionamiento
    de la función calcular_credito bajo distintos escenarios.
    """

    # CASOS NORMALES: Validan comportamiento esperado en condiciones estándar.

    def test_normal_1(self):
        # Verifica cálculo con valores típicos de crédito.
        cuota, total, saldo = logica_calculohipoteca_comentado.calcular_credito(
            300_000_000, 8, 20, 40, 70
        )

        self.assertAlmostEqual(cuota, 1_003_728, delta=5000)
        self.assertAlmostEqual(total, 240_894_740, delta=100000)
        self.assertAlmostEqual(saldo, 559_314_857, delta=200000)

    def test_normal_2(self):
        # Segundo escenario estándar para validar consistencia en resultados.
        cuota, total, saldo = logica_calculohipoteca_comentado.calcular_credito(
            450_000_000, 7, 18, 38, 72
        )

        self.assertAlmostEqual(cuota, 1_177_585, delta=5000)
        self.assertAlmostEqual(total, 254_358_389, delta=100000)
        self.assertAlmostEqual(saldo, 488_062_221, delta=200000)


        
    def test_normal_3(self):
        # Tercer escenario estándar para validar consistencia en resultados.
        cuota, total, saldo = logica_calculohipoteca_comentado.calcular_credito(
            380_000_000, 7, 25, 35, 75
        )

        self.assertAlmostEqual(cuota, 1_113_177, delta=5000)
        self.assertAlmostEqual(total, 333_953_171, delta=100000)
        self.assertAlmostEqual(saldo, 854_820_641, delta=200000)


    # CASOS EXTRAORDINARIOS: Evalúan límites altos o situaciones poco comunes.

    def test_vivienda_muy_costosa(self):
        # Prueba con inmueble de alto valor.
        cuota, total, saldo = logica_calculohipoteca_comentado.calcular_credito(
            900_000_000, 7.55, 15, 30, 80
        )

        self.assertAlmostEqual(cuota, 2_510_611, delta=5000)
        self.assertAlmostEqual(total, 451_909_995, delta=100000)
        self.assertAlmostEqual(saldo, 804_488_768, delta=200000)

    def test_plazo_muy_largo(self):
        # Evalúa comportamiento con plazo extendido.
        cuota, total, saldo = logica_calculohipoteca_comentado.calcular_credito(
            350_000_000, 8, 30, 45, 72
        )

        self.assertAlmostEqual(cuota, 1_155_679, delta=5000)
        self.assertAlmostEqual(total, 416_044_513, delta=100000)
        self.assertAlmostEqual(saldo, 1_584_868_460, delta=300000)

    def test_financiacion_alta(self):
        # Prueba con porcentaje financiado elevado.
        cuota, total, saldo = logica_calculohipoteca_comentado.calcular_credito(
            250_000_000, 9, 20, 70, 68
        )

        self.assertAlmostEqual(cuota, 1_574_520, delta=5000)
        self.assertAlmostEqual(total, 377_884_901, delta=100000)
        self.assertAlmostEqual(saldo, 980_771_884, delta=200000)

    def test_interes_muy_bajo(self):
        # Evalúa escenario con tasa reducida.
        cuota, total, saldo = logica_calculohipoteca_comentado.calcular_credito(
            400_000_000, 5, 20, 40, 78
        )

        self.assertAlmostEqual(cuota, 1_055_929, delta=5000)
        self.assertAlmostEqual(total, 253_423_004, delta=100000)
        self.assertAlmostEqual(saldo, 424_527_633, delta=200000)

    def test_persona_muy_mayor(self):
        # Caso con edad avanzada y plazo corto.
        cuota, total, saldo = logica_calculohipoteca_comentado.calcular_credito(
            280_000_000, 8, 10, 50, 85
        )

        self.assertAlmostEqual(cuota, 1_698_586, delta=5000)
        self.assertAlmostEqual(total, 203_830_359, delta=100000)
        self.assertAlmostEqual(saldo, 302_249_500, delta=200000)

    def test_vivienda_economica(self):
        # Prueba con inmueble de bajo valor.
        cuota, total, saldo = logica_calculohipoteca_comentado.calcular_credito(
            150_000_000, 9, 25, 60, 70
        )

        self.assertAlmostEqual(cuota, 755_277, delta=5000)
        self.assertAlmostEqual(total, 226_583_018, delta=100000)
        self.assertAlmostEqual(saldo, 776_077_259, delta=200000)


    # CASOS DE ERROR: Verifican que las validaciones funcionen correctamente.

    def test_error_edad(self):
        # Debe retornar error si la edad es menor a 65.
        with self.assertRaises(logica_calculohipoteca_comentado.Error_edad):
            logica_calculohipoteca_comentado.calcular_credito(
            300_000_000, 8, 20, 40, 50)
        

    

    def test_error_porcentaje_mayor_100(self):
        # Debe retornar error si el porcentaje supera el 100%.
        with self.assertRaises( logica_calculohipoteca_comentado.Eror_porcentaje):
         logica_calculohipoteca_comentado.calcular_credito(
            350_000_000, 7, 25, 120, 70
        )

        

    def test_error_porcentaje_negativo(self):
        # Debe retornar error si el porcentaje es negativo.
        with self.assertRaises( logica_calculohipoteca_comentado.Eror_porcentaje):
            logica_calculohipoteca_comentado.calcular_credito(
            280_000_000, 8, 20, -30, 72
        )

       

    def test_error_tasa_negativa(self):
        # Debe retornar error si la tasa es menor o igual a 0.
        with self.assertRaises(logica_calculohipoteca_comentado.Error_tasa_negativa):
            logica_calculohipoteca_comentado.calcular_credito(
            400_000_000, -5, 20, 40, 75
        )

        

if __name__ == '__main__':
    unittest.main()

import unittest
import logica_calculohipoteca


class TestCalculadoraHipoteca(unittest.TestCase):

    # ===============================
    # CASOS NORMALES
    # ===============================

    def test_normal_1(self):
        cuota, total, saldo = logica_calculohipoteca.calcular_credito(
            300_000_000, 8, 20, 40, 70
        )

        self.assertAlmostEqual(cuota, 1_003_728, delta=5000)
        self.assertAlmostEqual(total, 240_894_740, delta=100000)
        self.assertAlmostEqual(saldo, 559_314_857, delta=200000)


    def test_normal_2(self):
        cuota, total, saldo = logica_calculohipoteca.calcular_credito(
            450_000_000, 7, 25, 35, 75
        )

        self.assertAlmostEqual(cuota, 1_113_177, delta=5000)
        self.assertAlmostEqual(total, 333_953_171, delta=100000)
        self.assertAlmostEqual(saldo, 854_820_641, delta=200000)


    # ===============================
    # CASOS EXTRAORDINARIOS
    # ===============================

    def test_vivienda_muy_costosa(self):
        cuota, total, saldo = logica_calculohipoteca.calcular_credito(
            900_000_000, 7.55, 15, 30, 80
        )

        self.assertAlmostEqual(cuota, 2_510_611, delta=5000)
        self.assertAlmostEqual(total, 451_909_995, delta=100000)
        self.assertAlmostEqual(saldo, 804_488_768, delta=200000)


    def test_plazo_muy_largo(self):
        cuota, total, saldo = logica_calculohipoteca.calcular_credito(
            350_000_000, 8, 30, 45, 72
        )

        self.assertAlmostEqual(cuota, 1_155_679, delta=5000)
        self.assertAlmostEqual(total, 416_044_513, delta=100000)
        self.assertAlmostEqual(saldo, 1_584_868_460, delta=300000)


    def test_financiacion_alta(self):
        cuota, total, saldo = logica_calculohipoteca.calcular_credito(
            250_000_000, 9, 20, 70, 68
        )

        self.assertAlmostEqual(cuota, 1_574_520, delta=5000)
        self.assertAlmostEqual(total, 377_884_901, delta=100000)
        self.assertAlmostEqual(saldo, 980_771_884, delta=200000)


    def test_interes_muy_bajo(self):
        cuota, total, saldo = logica_calculohipoteca.calcular_credito(
            400_000_000, 5, 20, 40, 78
        )

        self.assertAlmostEqual(cuota, 1_055_929, delta=5000)
        self.assertAlmostEqual(total, 253_423_004, delta=100000)
        self.assertAlmostEqual(saldo, 424_527_633, delta=200000)


    def test_persona_muy_mayor(self):
        cuota, total, saldo = logica_calculohipoteca.calcular_credito(
            280_000_000, 8, 10, 50, 85
        )

        self.assertAlmostEqual(cuota, 1_698_586, delta=5000)
        self.assertAlmostEqual(total, 203_830_359, delta=100000)
        self.assertAlmostEqual(saldo, 302_249_500, delta=200000)


    def test_vivienda_economica(self):
        cuota, total, saldo = logica_calculohipoteca.calcular_credito(
            150_000_000, 9, 25, 60, 70
        )

        self.assertAlmostEqual(cuota, 755_277, delta=5000)
        self.assertAlmostEqual(total, 226_583_018, delta=100000)
        self.assertAlmostEqual(saldo, 776_077_259, delta=200000)


    # ===============================
    # CASOS DE ERROR
    # ===============================

    def test_error_edad(self):
        resultado = logica_calculohipoteca.calcular_credito(
            300_000_000, 8, 20, 40, 50
        )

        self.assertEqual(
            resultado,
            "Error: la edad mínima para solicitar hipoteca inversa es de 65 años."
        )


    def test_error_porcentaje_mayor_100(self):
        resultado = logica_calculohipoteca.calcular_credito(
            350_000_000, 7, 25, 120, 70
        )

        self.assertEqual(
            resultado,
            "Error: el porcentaje financiado debe ser entre 0 y 100."
        )


    def test_error_porcentaje_negativo(self):
        resultado = logica_calculohipoteca.calcular_credito(
            280_000_000, 8, 20, -30, 72
        )

        self.assertEqual(
            resultado,
            "Error: el porcentaje financiado debe ser entre 0 y 100."
        )


    def test_error_tasa_negativa(self):
        resultado = logica_calculohipoteca.calcular_credito(
            400_000_000, -5, 20, 40, 75
        )

        self.assertEqual(
            resultado,
            "Error: la tasa de interés debe ser mayor a 0."
        )


if __name__ == '__main__':
    unittest.main()


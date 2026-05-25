import sys
sys.path.append("src")
 
from model import logica_calculohipoteca_comentado 
from model.logica_calculohipoteca_comentado import credito , calculadora_hipoteca_inversa
import unittest
 
 
 
class TestCalculadoraHipoteca(unittest.TestCase):
    """
    Pruebas unitarias para verificar el correcto funcionamiento
    de la función calcular_credito bajo distintos escenarios.
    """
 
    # =========================
    # CASOS NORMALES
    # =========================
 
    def test_normal_1(self):
        test1 = credito("1000000001", 300_000_000, 8, 20, 40, 70)
        cuota = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(test1)
        total = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(test1)
        saldo = calculadora_hipoteca_inversa.calcular_saldo_proyectado(test1)
 
        self.assertAlmostEqual(cuota, 1_003_728, delta=5000)
        self.assertAlmostEqual(total, 240_894_740, delta=100000)
        self.assertAlmostEqual(saldo, 559_314_857, delta=200000)
 
    def test_normal_2(self):
        test2 = credito("1000000002", 450_000_000, 7, 25, 35, 75)
        cuota = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(test2)
        total = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(test2)
        saldo = calculadora_hipoteca_inversa.calcular_saldo_proyectado(test2)
        
        self.assertAlmostEqual(cuota, 1_113_177, delta=5000)
        self.assertAlmostEqual(total, 333_953_171, delta=100000)
        self.assertAlmostEqual(saldo, 854_820_641, delta=200000)
 
    def test_normal_3(self):
        test3 = credito("1000000003", 380_000_000, 7, 18, 38, 72)
        cuota = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(test3)
        total = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(test3)
        saldo = calculadora_hipoteca_inversa.calcular_saldo_proyectado(test3)
       
        self.assertAlmostEqual(cuota, 1_177_585, delta=5000)
        self.assertAlmostEqual(total, 254_358_389, delta=100000)
        self.assertAlmostEqual(saldo, 488_062_221, delta=200000)
 
    # =========================
    # CASOS EXTRAORDINARIOS
    # =========================
 
    def test_vivienda_muy_costosa(self):
        test4 = credito("1000000004", 900_000_000, 7.55, 15, 30, 80)
        cuota = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(test4)
        total = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(test4)
        saldo = calculadora_hipoteca_inversa.calcular_saldo_proyectado(test4)
       
        self.assertAlmostEqual(cuota, 2_510_611, delta=5000)
        self.assertAlmostEqual(total, 451_909_995, delta=100000)
        self.assertAlmostEqual(saldo, 804_488_768, delta=200000)
 
    def test_plazo_muy_largo(self):
        test5 = credito("1000000005", 350_000_000, 8, 30, 45, 72)
        cuota = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(test5)
        total = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(test5)
        saldo = calculadora_hipoteca_inversa.calcular_saldo_proyectado(test5)
 
        self.assertAlmostEqual(cuota, 1_155_679, delta=5000)
        self.assertAlmostEqual(total, 416_044_513, delta=100000)
        self.assertAlmostEqual(saldo, 1_584_868_460, delta=300000)
 
    def test_financiacion_alta(self):
        test6 = credito("1000000006", 250_000_000, 9, 20, 70, 68)
        cuota = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(test6)
        total = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(test6)
        saldo = calculadora_hipoteca_inversa.calcular_saldo_proyectado(test6)
        
        self.assertAlmostEqual(cuota, 1_574_520, delta=5000)
        self.assertAlmostEqual(total, 377_884_901, delta=100000)
        self.assertAlmostEqual(saldo, 980_771_884, delta=200000)
 
    def test_interes_muy_bajo(self):
        test7 = credito("1000000007", 400_000_000, 5, 20, 40, 78)
        cuota = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(test7)
        total = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(test7)
        saldo = calculadora_hipoteca_inversa.calcular_saldo_proyectado(test7)
 
        self.assertAlmostEqual(cuota, 1_055_929, delta=5000)
        self.assertAlmostEqual(total, 253_423_004, delta=100000)
        self.assertAlmostEqual(saldo, 424_527_633, delta=200000)
 
    def test_persona_muy_mayor(self):
        test8 = credito("1000000008", 280_000_000, 8, 10, 50, 85)
        cuota = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(test8)
        total = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(test8)
        saldo = calculadora_hipoteca_inversa.calcular_saldo_proyectado(test8)
 
        self.assertAlmostEqual(cuota, 1_698_586, delta=5000)
        self.assertAlmostEqual(total, 203_830_359, delta=100000)
        self.assertAlmostEqual(saldo, 302_249_500, delta=200000)
 
    def test_vivienda_economica(self):
        test9 = credito("1000000009", 150_000_000, 9, 25, 60, 70)
        cuota = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(test9)
        total = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(test9)
        saldo = calculadora_hipoteca_inversa.calcular_saldo_proyectado(test9)
 
        self.assertAlmostEqual(cuota, 755_277, delta=5000)
        self.assertAlmostEqual(total, 226_583_018, delta=100000)
        self.assertAlmostEqual(saldo, 776_077_259, delta=200000)
 
    # =========================
    # CASOS DE ERROR
    # =========================
 
    def test_error_edad(self):
        with self.assertRaises(logica_calculohipoteca_comentado.ErrorEdad):
            test10 = credito("1000000010", 300_000_000, 8, 20, 40, 50)
            calculadora_hipoteca_inversa.validar_edad(test10.edad)
 
    def test_error_porcentaje_mayor_100(self):
        with self.assertRaises(logica_calculohipoteca_comentado.ErrorPorcentaje):
            test11 = credito("1000000011", 350_000_000, 7, 25, 120, 70)
            calculadora_hipoteca_inversa.validar_porcetanje_LTV_mayor_100(test11.porcentaje_LTV)
 
    def test_error_porcentaje_negativo(self):
        with self.assertRaises(logica_calculohipoteca_comentado.ErrorPorcentaje):
            test12 = credito("1000000012", 280_000_000, 8, 20, -30, 72)
            calculadora_hipoteca_inversa.validar_porcetanje_LTV_menor_0(test12.porcentaje_LTV)
 
    def test_error_tasa_negativa(self):
        with self.assertRaises(logica_calculohipoteca_comentado.ErrorTasaNegativa):
            test13 = credito("1000000013", 400_000_000, -5, 20, 40, 75)
            calculadora_hipoteca_inversa.validar_tasa_capitalizacion(test13.tasa_capitalizacion)
 
    def test_error_plazo(self):
        with self.assertRaises(logica_calculohipoteca_comentado.ErrorPlazo):
            test14 = credito("1000000014", 300_000_000, 8, 0, 40, 70)
            calculadora_hipoteca_inversa.validar_plazo_simulacion(test14.plazo_simulacion)
 
    def test_error_valor_inmueble(self):
        with self.assertRaises(logica_calculohipoteca_comentado.ErrorValorInmueble):
            test15 = credito("1000000015", 0, 8, 20, 40, 70)
            calculadora_hipoteca_inversa.validar_valor_inmueble(test15.valor_inmueble)
 
 
if __name__ == '__main__':
    unittest.main()
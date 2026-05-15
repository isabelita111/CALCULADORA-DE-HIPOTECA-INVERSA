import unittest
import sys
sys.path.append("src")
 
from model.calculos import Calculo
from controller.calculos_controller import calculosController
 
 
class TestCalculos(unittest.TestCase):
 
    # Test Fixture: se ejecuta una sola vez antes de todos los tests
    def setUpClass():
        calculosController.eliminar_tabla()
        calculosController.crear_tabla()
 
    # ========================
    # CASOS DE INSERTAR
    # ========================
 
    def test_insertar_y_buscar_1(self):
        """Caso normal 1: vivienda 300M, tasa 8%, edad 70, plazo 20 años, LTV 40%"""
        calculo_prueba = Calculo(
            cedula="1000111001",
            valor_inmueble=300_000_000,
            tasa_capitalizacion=0.08,
            edad=70,
            plazo_simulacion=20,
            porcentaje_LTV=0.40,
            monto_mensual_recibido=0,
            total_recibido_acumulado=0,
            saldo_proyectado=0
        )
        calculosController.insertar(calculo_prueba)
        calculo_buscado = calculosController.buscar_cedula(cedula="1000111001")
        self.assertIsNotNone(calculo_buscado)
        self.assertEqual(calculo_buscado.cedula, calculo_prueba.cedula)
        self.assertEqual(calculo_buscado.valor_inmueble, calculo_prueba.valor_inmueble)
 
    def test_insertar_y_buscar_2(self):
        """Caso normal 2: vivienda 450M, tasa 7%, edad 75, plazo 25 años, LTV 35%"""
        calculo_prueba = Calculo(
            cedula="1000111002",
            valor_inmueble=450_000_000,
            tasa_capitalizacion=0.07,
            edad=75,
            plazo_simulacion=25,
            porcentaje_LTV=0.35,
            monto_mensual_recibido=0,
            total_recibido_acumulado=0,
            saldo_proyectado=0
        )
        calculosController.insertar(calculo_prueba)
        calculo_buscado = calculosController.buscar_cedula(cedula=calculo_prueba.cedula)
        self.assertIsNotNone(calculo_buscado)
        self.assertEqual(calculo_buscado.cedula, calculo_prueba.cedula)
 
    def test_insertar_y_buscar_3(self):
        """Caso normal 3: vivienda 380M, tasa 7%, edad 72, plazo 18 años, LTV 38%"""
        calculo_prueba = Calculo(
            cedula="1000111003",
            valor_inmueble=380_000_000,
            tasa_capitalizacion=0.07,
            edad=72,
            plazo_simulacion=18,
            porcentaje_LTV=0.38,
            monto_mensual_recibido=0,
            total_recibido_acumulado=0,
            saldo_proyectado=0
        )
        calculosController.insertar(calculo_prueba)
        calculo_buscado = calculosController.buscar_cedula(cedula=calculo_prueba.cedula)
        self.assertIsNotNone(calculo_buscado)
        self.assertEqual(calculo_buscado.cedula, calculo_prueba.cedula)
 
    # ========================
    # CASOS DE BUSCAR
    # ========================
 
    def test_buscar_cedula_no_existe(self):
        """Error: buscar una cédula que no está registrada en la BD"""
        self.assertRaises(Exception, calculosController.buscar_cedula, "9999999999")
 
    def test_llave_primaria(self):
        """Error: no se pueden insertar dos calculos con la misma cédula (PK)"""
        calculo_original = Calculo(
            cedula="1000111004",
            valor_inmueble=380_000_000,
            tasa_capitalizacion=0.07,
            edad=72,
            plazo_simulacion=18,
            porcentaje_LTV=0.38,
            monto_mensual_recibido=0,
            total_recibido_acumulado=0,
            saldo_proyectado=0
        )
        calculosController.insertar(calculo_original)
        calculo_duplicado = Calculo(
            cedula="1000111004",
            valor_inmueble=900_000_000,
            tasa_capitalizacion=0.0755,
            edad=80,
            plazo_simulacion=15,
            porcentaje_LTV=0.30,
            monto_mensual_recibido=0,
            total_recibido_acumulado=0,
            saldo_proyectado=0
        )
        self.assertRaises(Exception, calculosController.insertar, calculo_duplicado)
 
    # ========================
    # CASOS DE MODIFICAR
    # ========================
 
    def test_actualizar_calculo(self):
        """Caso normal: actualizar el valor del inmueble y el plazo de un calculo existente"""
        calculo_original = Calculo(
            cedula="2000222001",
            valor_inmueble=300_000_000,
            tasa_capitalizacion=0.08,
            edad=70,
            plazo_simulacion=20,
            porcentaje_LTV=0.40,
            monto_mensual_recibido=0,
            total_recibido_acumulado=0,
            saldo_proyectado=0
        )
        calculosController.insertar(calculo_original)
 
        calculo_actualizado = Calculo(
            cedula="2000222001",
            valor_inmueble=350_000_000,
            tasa_capitalizacion=0.08,
            edad=70,
            plazo_simulacion=25,
            porcentaje_LTV=0.40,
            monto_mensual_recibido=0,
            total_recibido_acumulado=0,
            saldo_proyectado=0
        )
        calculosController.actualizar(calculo_actualizado)
 
        calculo_buscado = calculosController.buscar_cedula("2000222001")
        self.assertEqual(calculo_buscado.valor_inmueble, calculo_actualizado.valor_inmueble)
        self.assertEqual(calculo_buscado.plazo_simulacion, calculo_actualizado.plazo_simulacion)
 
    def test_eliminar_calculo(self):
        """Caso normal: eliminar un calculo existente de la BD"""
        calculo = Calculo(
            cedula="2000222002",
            valor_inmueble=250_000_000,
            tasa_capitalizacion=0.09,
            edad=68,
            plazo_simulacion=20,
            porcentaje_LTV=0.70,
            monto_mensual_recibido=0,
            total_recibido_acumulado=0,
            saldo_proyectado=0
        )
        calculosController.insertar(calculo)
        calculosController.eliminar(cedula="2000222002")
        self.assertRaises(Exception, calculosController.buscar_cedula, "2000222002")
 
    def test_actualizar_calculo_no_existe(self):
        """Error: actualizar un calculo con una cédula que no existe en la BD"""
        calculo_inexistente = Calculo(
            cedula="8888888888",
            valor_inmueble=400_000_000,
            tasa_capitalizacion=0.08,
            edad=65,
            plazo_simulacion=20,
            porcentaje_LTV=0.50,
            monto_mensual_recibido=0,
            total_recibido_acumulado=0,
            saldo_proyectado=0
        )
        self.assertRaises(Exception, calculosController.actualizar, calculo_inexistente)
 
 
if __name__ == '__main__':
    unittest.main()
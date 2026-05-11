import unittest
import sys
sys.path.append("src")
 
from model.salidas import Salidas
from controller.salidas_controller import SalidasController
 
 
class TestSalidas(unittest.TestCase):
 
    
    def setUpClass():
        SalidasController.eliminar_tabla()
        SalidasController.crear_tabla()
 
    
    # CASOS DE INSERTAR
    
 
    def test_insertar_y_buscar_1(self):
        """Caso normal 1: vivienda 300M, tasa 8%, plazo 20 años, LTV 40%"""
        salida_prueba = Salidas(
            id_calculo="CAL-001",
            monto_mensual_recibido=1_003_728.0,
            total_recibido_acumulado=240_894_740.0,
            saldo_proyectado=559_314_857.0
        )
        SalidasController.insertar(salida_prueba)
        salida_buscada = SalidasController.buscar_salidas(id_calculo="CAL-001")
        self.assertTrue(salida_buscada.is_equal(salida_prueba))
 
    def test_insertar_y_buscar_2(self):
        """Caso normal 2: vivienda 450M, tasa 7%, plazo 25 años, LTV 35%"""
        salida_prueba = Salidas(
            id_calculo="CAL-002",
            monto_mensual_recibido=1_113_177.0,
            total_recibido_acumulado=333_953_171.0,
            saldo_proyectado=854_820_641.0
        )
        SalidasController.insertar(salida_prueba)
        salida_buscada = SalidasController.buscar_salidas(id_calculo=salida_prueba.id_calculo)
        self.assertTrue(salida_buscada.is_equal(salida_prueba))
 
    def test_insertar_y_buscar_3(self):
        """Caso normal 3: vivienda 380M, tasa 7%, plazo 18 años, LTV 38%"""
        salida_prueba = Salidas(
            id_calculo="CAL-003",
            monto_mensual_recibido=1_177_585.0,
            total_recibido_acumulado=254_358_389.0,
            saldo_proyectado=488_062_221.0
        )
        SalidasController.insertar(salida_prueba)
        salida_buscada = SalidasController.buscar_salidas(id_calculo=salida_prueba.id_calculo)
        self.assertTrue(salida_buscada.is_equal(salida_prueba))
 
    
    
    # CASOS DE BUSCAR
   
 
    def test_buscar_id_no_existe(self):
        """Error: buscar un id_calculo que no está registrado en la BD"""
        self.assertRaises(Exception, SalidasController.buscar_salidas, "CAL-999")
 
    def test_llave_primaria(self):
        """Error: no se pueden insertar dos salidas con el mismo id_calculo """
        salida_original = Salidas(
            id_calculo="CAL-004",
            monto_mensual_recibido=755_277.0,
            total_recibido_acumulado=226_583_018.0,
            saldo_proyectado=776_077_259.0
        )
        SalidasController.insertar(salida_original)
        salida_duplicada = Salidas(
            id_calculo="CAL-004",
            monto_mensual_recibido=1_574_520.0,
            total_recibido_acumulado=377_884_901.0,
            saldo_proyectado=980_771_884.0
        )
        self.assertRaises(Exception, SalidasController.insertar, salida_duplicada)
 
   
    # CASOS DE MODIFICAR
   
 
    def test_actualizar_salida(self):
        """Caso normal: actualizar el monto mensual y el saldo de una salida existente"""
        # Primero insertar
        salida_original = Salidas(
            id_calculo="CAL-005",
            monto_mensual_recibido=1_003_728.0,
            total_recibido_acumulado=240_894_740.0,
            saldo_proyectado=559_314_857.0
        )
        SalidasController.insertar(salida_original)
 
        # Modificar con nuevos datos
        salida_actualizada = Salidas(
            id_calculo="CAL-005",
            monto_mensual_recibido=1_155_679.0,
            total_recibido_acumulado=416_044_513.0,
            saldo_proyectado=1_584_868_460.0
        )
        SalidasController.actualizar(salida_actualizada)
 
        # Verificar que los cambios quedaron guardados
        salida_buscada = SalidasController.buscar_salidas("CAL-005")
        self.assertTrue(salida_buscada.is_equal(salida_actualizada))
 
    def test_eliminar_salida(self):
        """Caso normal: eliminar una salida existente de la BD"""
        # Primero insertar
        salida = Salidas(
            id_calculo="CAL-006",
            monto_mensual_recibido=755_277.0,
            total_recibido_acumulado=226_583_018.0,
            saldo_proyectado=776_077_259.0
        )
        SalidasController.insertar(salida)
 
        # Eliminar
        SalidasController.eliminar(id_calculo="CAL-006")
 
        # Verificar que ya no existe
        self.assertRaises(Exception, SalidasController.buscar_salidas, "CAL-006")
 
    def test_actualizar_salida_no_existe(self):
        """Error: actualizar una salida con un id_calculo que no existe en la BD"""
        salida_inexistente = Salidas(
            id_calculo="CAL-999",
            monto_mensual_recibido=999_999.0,
            total_recibido_acumulado=111_111_111.0,
            saldo_proyectado=222_222_222.0
        )
        self.assertRaises(Exception, SalidasController.actualizar, salida_inexistente)
 
 
if __name__ == '__main__':
    unittest.main()
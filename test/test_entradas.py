import unittest
import sys
sys.path.append("src")
 
from model.entradas import Entrada
from controller.entradas_controller import EntradasController
 
 
class TestEntradas(unittest.TestCase):
 
    
    def setUpClass():
        EntradasController.eliminar_tabla()
        EntradasController.crear_tabla()
 
    
    # CASOS DE INSERTAR
    
 
    def test_insertar_y_buscar_1(self):
        """Caso normal 1: vivienda 300M, tasa 8%, edad 70, plazo 20 años, LTV 40%"""
        entrada_prueba = Entrada(
            cedula="1000111001",
            valor_inmueble=300_000_000,
            tasa_capitalizacion=0.08,
            edad=70,
            plazo_simulacion=20,
            porcentaje_LTV=0.40
        )
        EntradasController.insertar(entrada_prueba)
        entrada_buscada = EntradasController.buscar_cedula(cedula="1000111001")
        self.assertTrue(entrada_buscada.is_equal(entrada_prueba))
 
    def test_insertar_y_buscar_2(self):
        """Caso normal 2: vivienda 450M, tasa 7%, edad 75, plazo 25 años, LTV 35%"""
        entrada_prueba = Entrada(
            cedula="1000111002",
            valor_inmueble=450_000_000,
            tasa_capitalizacion=0.07,
            edad=75,
            plazo_simulacion=25,
            porcentaje_LTV=0.35
        )
        EntradasController.insertar(entrada_prueba)
        entrada_buscada = EntradasController.buscar_cedula(cedula=entrada_prueba.cedula)
        self.assertTrue(entrada_buscada.is_equal(entrada_prueba))
 
    def test_insertar_y_buscar_3(self):
        """Caso normal 3: vivienda 380M, tasa 7%, edad 72, plazo 18 años, LTV 38%"""
        entrada_prueba = Entrada(
            cedula="1000111004",
            valor_inmueble=380_000_000,
            tasa_capitalizacion=0.07,
            edad=72,
            plazo_simulacion=18,
            porcentaje_LTV=0.38
        )
        EntradasController.insertar(entrada_prueba)
        entrada_buscada = EntradasController.buscar_cedula(cedula=entrada_prueba.cedula)
        self.assertTrue(entrada_buscada.is_equal(entrada_prueba))
 
    
    # CASOS DE BUSCAR
    
 
    def test_buscar_cedula_no_existe(self):
        """Error: buscar una cédula que no está registrada en la BD"""
        self.assertRaises(Exception, EntradasController.buscar_cedula, "9999999999")
 
    def test_llave_primaria(self):
        """Error: no se pueden insertar dos entradas con la misma cédula (PK)"""
        entrada_original = Entrada(
            cedula="1000111003",
            valor_inmueble=380_000_000,
            tasa_capitalizacion=0.07,
            edad=72,
            plazo_simulacion=18,
            porcentaje_LTV=0.38
        )
        EntradasController.insertar(entrada_original)
        entrada_duplicada = Entrada(
            cedula="1000111003",
            valor_inmueble=900_000_000,
            tasa_capitalizacion=0.0755,
            edad=80,
            plazo_simulacion=15,
            porcentaje_LTV=0.30
        )
        self.assertRaises(Exception, EntradasController.insertar, entrada_duplicada)
 
    
    # CASOS DE MODIFICAR
   
 
    def test_actualizar_entrada(self):
        """Caso normal: actualizar el valor del inmueble y el plazo de una entrada existente"""
        # Primero insertar
        entrada_original = Entrada(
            cedula="2000222001",
            valor_inmueble=300_000_000,
            tasa_capitalizacion=0.08,
            edad=70,
            plazo_simulacion=20,
            porcentaje_LTV=0.40
        )
        EntradasController.insertar(entrada_original)
 
        # Modificar con nuevos datos
        entrada_actualizada = Entrada(
            cedula="2000222001",
            valor_inmueble=350_000_000,
            tasa_capitalizacion=0.08,
            edad=70,
            plazo_simulacion=25,
            porcentaje_LTV=0.40
        )
        EntradasController.actualizar(entrada_actualizada)
 
        # Verificar que los cambios quedaron guardados
        entrada_buscada = EntradasController.buscar_cedula("2000222001")
        self.assertTrue(entrada_buscada.is_equal(entrada_actualizada))
 
    def test_eliminar_entrada(self):
        """Caso normal: eliminar una entrada existente de la BD"""
        # Primero insertar
        entrada = Entrada(
            cedula="2000222002",
            valor_inmueble=250_000_000,
            tasa_capitalizacion=0.09,
            edad=68,
            plazo_simulacion=20,
            porcentaje_LTV=0.70
        )
        EntradasController.insertar(entrada)
 
        # Eliminar
        EntradasController.eliminar(cedula="2000222002")
 
        # Verificar que ya no existe
        self.assertRaises(Exception, EntradasController.buscar_cedula, "2000222002")
 
    def test_actualizar_entrada_no_existe(self):
        """Error: actualizar una entrada con una cédula que no existe en la BD"""
        entrada_inexistente = Entrada(
            cedula="8888888888",
            valor_inmueble=400_000_000,
            tasa_capitalizacion=0.08,
            edad=65,
            plazo_simulacion=20,
            porcentaje_LTV=0.50
        )
        self.assertRaises(Exception, EntradasController.actualizar, entrada_inexistente)
 
 
if __name__ == '__main__':
    unittest.main()
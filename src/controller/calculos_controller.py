import sys
sys.path.append("src")

import psycopg2
from model.calculos import Calculo
import secret_config

from model.logica_calculohipoteca_comentado import calculadora_hipoteca_inversa

class calculosController:

    def crear_tabla():
        cursor = calculosController.obtener_cursor()
        with open("sql/crear-calculos.sql", "r") as archivo:
            sql = archivo.read()
        cursor.execute(sql)
        cursor.connection.commit()

    def eliminar_tabla():
        cursor = calculosController.obtener_cursor()
        with open("sql/borrar-calculos.sql", "r") as archivo:
            sql = archivo.read()    
        cursor.execute(sql)
        cursor.connection.commit()
        

    def insertar(calculos: Calculo):
        cursor = calculosController.obtener_cursor()
        monto_mensual_recibido = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(calculos)
        total_recibido_acumulado = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(calculos)
        saldo_proyectado = calculadora_hipoteca_inversa.calcular_saldo_proyectado(calculos)
        cursor.execute("""
            INSERT INTO calculos 
            (cedula, valor_inmueble, tasa_capitalizacion, edad, plazo_simulacion, porcentaje_LTV, monto_mensual_recibido, total_recibido_acumulado, saldo_proyectado)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            calculos.cedula,
            calculos.valor_inmueble,
            calculos.tasa_capitalizacion,
            calculos.edad,
            calculos.plazo_simulacion,
            calculos.porcentaje_LTV,
            monto_mensual_recibido,
            total_recibido_acumulado,
            saldo_proyectado
        ))
        cursor.connection.commit()

    def buscar_cedula(cedula):
        cursor = calculosController.obtener_cursor()

        cursor.execute("""
            SELECT cedula, valor_inmueble, tasa_capitalizacion, edad, plazo_simulacion, porcentaje_LTV, monto_mensual_recibido, total_recibido_acumulado, saldo_proyectado
            FROM calculos 
            WHERE cedula = %s
        """, (cedula,))

        fila = cursor.fetchone()
        resultado = Calculo(
            cedula=fila[0],
            valor_inmueble=fila[1],
            tasa_capitalizacion=fila[2],
            edad=fila[3],
            plazo_simulacion=fila[4],
            porcentaje_LTV=fila[5],
            monto_mensual_recibido=fila[6],
            total_recibido_acumulado=fila[7],
            saldo_proyectado=fila[8]            
        )
        return resultado

   
    def actualizar(calculos: Calculo):
        cursor = calculosController.obtener_cursor()
        monto_mensual_recibido = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(calculos)
        total_recibido_acumulado = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(calculos)
        saldo_proyectado = calculadora_hipoteca_inversa.calcular_saldo_proyectado(calculos)
        cursor.execute("""
            UPDATE calculos
            SET valor_inmueble = %s,
                tasa_capitalizacion = %s,
                edad = %s,
                plazo_simulacion = %s,
                porcentaje_LTV = %s,
                monto_mensual_recibido = %s,
                total_recibido_acumulado = %s,
                saldo_proyectado = %s
            WHERE cedula = %s
        """, (
            calculos.valor_inmueble,
            calculos.tasa_capitalizacion,
            calculos.edad,
            calculos.plazo_simulacion,
            calculos.porcentaje_LTV,
            monto_mensual_recibido,
            total_recibido_acumulado,
            saldo_proyectado,
            calculos.cedula
        ))
        if cursor.rowcount == 0:
            raise Exception("La cédula no existe en la base de datos")
        cursor.connection.commit()


    def eliminar(cedula):
        cursor = calculosController.obtener_cursor()
        with open("sql/eliminar-calculos.sql", "r") as archivo:
            sql = archivo.read()
        cursor.execute(sql, (cedula,))
        cursor.connection.commit()

    def obtener_cursor():
        connection = psycopg2.connect(
            database=secret_config.PGDATABASE,
            user=secret_config.PGUSER,
            password=secret_config.PGPASSWORD,
            host=secret_config.PGHOST,
            port=secret_config.PGPORT
        )
        cursor = connection.cursor()
        return cursor


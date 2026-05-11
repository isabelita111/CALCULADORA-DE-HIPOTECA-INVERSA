import sys
sys.path.append(".")
sys.path.append("src")

import psycopg2
from model.salidas import Salidas
import secret_config    

class SalidasController:

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
    
 
    def eliminar_tabla():
        cursor = SalidasController.obtener_cursor()
        cursor.execute("""DROP TABLE IF EXISTS salidas""")
        cursor.connection.commit()
    
   
    def crear_tabla():
        cursor = SalidasController.obtener_cursor()
        cursor.execute("""
            CREATE TABLE salidas (
                id_calculo VARCHAR(50) NOT NULL PRIMARY KEY,
                monto_mensual_recibido FLOAT NOT NULL,
                total_recibido_acumulado FLOAT NOT NULL,
                saldo_proyectado FLOAT NOT NULL
            )
        """)
        cursor.connection.commit()

    
    def insertar(salidas: Salidas):
        cursor = SalidasController.obtener_cursor()
        cursor.execute("""
            INSERT INTO salidas 
            (id_calculo, monto_mensual_recibido, total_recibido_acumulado, saldo_proyectado)
            VALUES (%s, %s, %s, %s)
        """, (
            salidas.id_calculo,
            salidas.monto_mensual_recibido,
            salidas.total_recibido_acumulado,
            salidas.saldo_proyectado
        ))
        cursor.connection.commit()

   
    def buscar_salidas(id_calculo: str) -> Salidas:
        cursor = SalidasController.obtener_cursor()

        cursor.execute("""
            SELECT id_calculo, monto_mensual_recibido, total_recibido_acumulado, saldo_proyectado
            FROM salidas
            WHERE id_calculo = %s
        """, (id_calculo,))

        fila = cursor.fetchone()

        resultado = Salidas(
            id_calculo=fila[0],
            monto_mensual_recibido=fila[1],
            total_recibido_acumulado=fila[2],
            saldo_proyectado=fila[3]
        )
        return resultado

   
    def actualizar(salidas: Salidas):
        cursor = SalidasController.obtener_cursor()
        cursor.execute("""
            UPDATE salidas
            SET monto_mensual_recibido = %s,
                total_recibido_acumulado = %s,
                saldo_proyectado = %s
            WHERE id_calculo = %s
        """, (
            salidas.monto_mensual_recibido,
            salidas.total_recibido_acumulado,
            salidas.saldo_proyectado,
            salidas.id_calculo
        ))

       
        if cursor.rowcount == 0:
            raise Exception("El id_calculo no existe en la base de datos")

        cursor.connection.commit()

   
    def eliminar(id_calculo: str):
        cursor = SalidasController.obtener_cursor()
        cursor.execute("""
            DELETE FROM salidas
            WHERE id_calculo = %s
        """, (id_calculo,))

        
        if cursor.rowcount == 0:
            raise Exception("El id_calculo no existe en la base de datos")

        cursor.connection.commit()

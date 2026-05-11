import sys
sys.path.append("src")

import psycopg2
from model.entradas import Entrada
import secret_config

class EntradasController:

    def crear_tabla():
        cursor = EntradasController.obtener_cursor()
        cursor.execute("""CREATE TABLE entradas (
                            cedula VARCHAR(20) NOT NULL primary key,
                            valor_inmueble FLOAT NOT NULL,
                            tasa_capitalizacion FLOAT NOT NULL,
                            edad INT NOT NULL,
                            plazo_simulacion INT NOT NULL,
                            porcentaje_LTV FLOAT NOT NULL
                        )""")
        cursor.connection.commit()

    def eliminar_tabla():
        cursor = EntradasController.obtener_cursor()
        cursor.execute("""DROP TABLE entradas""")
        cursor.connection.commit()
        

    def insertar(entradas: Entrada):
        cursor = EntradasController.obtener_cursor()
        cursor.execute("""
            INSERT INTO entradas 
            (cedula, valor_inmueble, tasa_capitalizacion, edad, plazo_simulacion, porcentaje_LTV)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            entradas.cedula,
            entradas.valor_inmueble,
            entradas.tasa_capitalizacion,
            entradas.edad,
            entradas.plazo_simulacion,
            entradas.porcentaje_LTV
        ))
        cursor.connection.commit()

    def buscar_cedula(cedula):
        cursor = EntradasController.obtener_cursor()

        cursor.execute("""
            SELECT cedula, valor_inmueble, tasa_capitalizacion, edad, plazo_simulacion, porcentaje_LTV 
            FROM entradas 
            WHERE cedula = %s
        """, (cedula,))

        fila = cursor.fetchone()
        resultado = Entrada(
            cedula=fila[0],
            valor_inmueble=fila[1],
            tasa_capitalizacion=fila[2],
            edad=fila[3],
            plazo_simulacion=fila[4],
            porcentaje_LTV=fila[5]
        )
        return resultado

   
    def actualizar(entradas: Entrada):
        cursor = EntradasController.obtener_cursor()
        cursor.execute("""
            UPDATE entradas
            SET valor_inmueble = %s,
                tasa_capitalizacion = %s,
                edad = %s,
                plazo_simulacion = %s,
                porcentaje_LTV = %s
            WHERE cedula = %s
        """, (
            entradas.valor_inmueble,
            entradas.tasa_capitalizacion,
            entradas.edad,
            entradas.plazo_simulacion,
            entradas.porcentaje_LTV,
            entradas.cedula
        ))
        if cursor.rowcount == 0:
            raise Exception("La cédula no existe en la base de datos")
        cursor.connection.commit()


    def eliminar(cedula):
        cursor = EntradasController.obtener_cursor()
        cursor.execute("""
            DELETE FROM entradas
            WHERE cedula = %s
        """, (cedula,))
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


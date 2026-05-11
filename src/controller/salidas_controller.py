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
    
    def crear_tabla():
        cursor = SalidasController.obtener_cursor()
        cursor.execute("""CREATE TABLE salidas (
                            id_calculo  NOT NULL primary key,
                            monto_mensual_recibido FLOAT NOT NULL,
                            total_recibido_acumulado FLOAT NOT NULL,
                            saldo_proyectado FLOAT NOT NULL
                            
                        )""")
        cursor.connection.commit()

    def insertar(salidas: Salidas):
        cursor = SalidasController.obtener_cursor()
        consulta = ("""insert into salidas (id_calculo, monto_mensual_recibido, total_recibido_acumulado, saldo_proyectado)
                        values ('{salidas.id_calculo}', {salidas.monto_mensual_recibido}, {salidas.total_recibido_acumulado}, {salidas.saldo_proyectado})""")
        cursor.execute(consulta)
        cursor.connection.commit()

    def buscar_salidas(id_calculo : str) -> Salidas:
        cursor = SalidasController.obtener_cursor()

        consulta = f"""select id_calculo, monto_mensual_recibido, total_recibido_acumulado, saldo_proyectado from salidas where id_calculo = '{id_calculo}'"""
        cursor.execute(consulta)

        fila =  cursor.fetchone()
        resultado = Salidas(id_calculo=fila[0], monto_mensual_recibido=fila[1], total_recibido_acumulado=fila[2], saldo_proyectado=fila[3])
        return resultado
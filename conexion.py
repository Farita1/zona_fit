import sys
import mysql.connector
from mysql.connector import pooling
from logger_base import log

class Conexion:

    _DATABASE = 'zona_fit'
    _USERNAME = 'root'
    _PASSWORD = ''
    _DB_PORT = 3306
    _HOST = '127.0.0.1'
    _POOL_NAME = 'zona_fit_pool'
    _POOL_SIZE = 5
    _pool = None
    
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pooling.MySQLConnectionPool(
                    pool_name=cls._POOL_NAME,
                    pool_size=cls._POOL_SIZE,
                    host=cls._HOST,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Creación del pool exitosa: {cls._POOL_NAME}')
                log.debug(f'Tamaño del pool: {cls._POOL_SIZE}')
            except mysql.connector.Error as e:
                log.error(f'Ocurrió un error al obtener el pool: {e}')
                sys.exit()
        return cls._pool

    @classmethod
    def obtenerConexion(cls):
        try:
            conexion = cls.obtenerPool().get_connection()
            log.debug(f'Conexión obtenida del pool: {conexion}')
            return conexion
        except mysql.connector.Error as e:
            log.error(f'Error al obtener conexión: {e}')
            return None
    
    @classmethod
    def liberarConexion(cls, conexion):
        if conexion:
            conexion.close()  # Se cierra la conexión para devolverla al pool
            log.debug(f'Conexión devuelta al pool: {conexion}')
        
    @classmethod
    def cerrarConexiones(cls):
        if cls._pool:
            cls._pool._remove_connections()  # Cierra todas las conexiones activas
            log.debug('Se han cerrado todas las conexiones del pool.')

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    if conexion1:
        Conexion.liberarConexion(conexion1)

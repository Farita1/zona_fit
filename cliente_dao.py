from logger_base import log
from cursor_del_pool import CursorDelPool
from cliente import Cliente
class ClienteDAO:
    
    _SELECCIONAR = 'SELECT * FROM clientes ORDER BY id'
    _INSERTAR = 'INSERT INTO clientes(nombre, apellido, membresia) VALUES (%s, %s, %s)'
    _ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM clientes WHERE id = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        
    @classmethod
    def insertar(cls, cliente):
        with CursorDelPool() as cursor:
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Cliente insertado: {cliente}')
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, cliente):
        with CursorDelPool as cursor:            
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Cliente actualizado: {cliente}')
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, cliente_id):
        with CursorDelPool() as cursor:
            valores = (cliente_id,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Cliente eliminado con ID: {cliente_id}')
            return cursor.rowcount


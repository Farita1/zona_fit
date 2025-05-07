from cliente import Cliente
from cliente_dao import ClienteDAO
from logger_base import log
opcion = None

while opcion != 5:
    print('ZONA FIT')
    print('1. Seleccionar todos los clientes')
    print('2. Agregar cliente')
    print('3. Actualizar cliente')
    print('4. Eliminar cliente')
    print('5. Salir')
    opcion = int(input('Elegir opción (1-5): '))
    
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        for cliente in clientes:
            log.info(cliente)
    elif opcion == 2:
        nombre_insertado = input('Ingrese el nombre del cliente: ')
        apellido_insertado = input('Ingrese el apellido del cliente: ')
        membresia_insertado = int(input('Ingrese el valor de la membresia del cliente: '))
        cliente_insertado = Cliente(nombre = nombre_insertado, apellido = apellido_insertado, memebresia = membresia_insertado)
        insertado = ClienteDAO.insertar(cliente_insertado)
        log.debug(cliente_insertado)
        
    elif opcion == 3:
        id_actualizado = int(input('Ingrese el id del cliente a actualizar: '))
        nombre_actualizado = input('Ingrese el nombre del cliente: ')
        apellido_actualizado = input('Ingresar el apellido del cliente: ')
        membresia_actualizado = int(input('Ingrese la membresia: '))
        cliente_actualizado = Cliente(nombre=nombre_actualizado, apellido = apellido_actualizado, memebresia = membresia_actualizado, id = id_actualizado)
        actualizado = ClienteDAO.actualizar(cliente_actualizado)
        log.debug(cliente_actualizado)
        
    elif opcion == 4:
        id_eliminado = int(input('Ingrese el id del cliente a eliminar: '))
        eliminado = ClienteDAO.eliminar(Cliente(id = id_eliminado))
        log.debug(eliminado)
        
    elif opcion == 5:
        log.debug('GRACIAS, HASTA LUEGO')

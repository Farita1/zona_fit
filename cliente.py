class Cliente:
    def __init__(self, id = None, nombre = None, apellido = None, memebresia = None):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._membresia = memebresia
        
    def __str__(self):
        return f'Cliente: {self._id}, {self._nombre}, {self._apellido}, {self._membresia}'
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        return self._s
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property
    def membresia(self):
        return self._membresia
    
    @membresia.setter
    def membresia(self, membresia):
        self._membresia = membresia

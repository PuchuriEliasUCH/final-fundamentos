class Area():
    def __init__(self, id, nombre):
        self.__id = id
        self.__nombre = nombre.title()
        self.__activo = True

    # ID
    @property    
    def id(self):
        return self.__id 

    # Nombre
    @property
    def nombre(self):
        return self.__nombre

    # Activo
    @property
    def activo(self):
        return self.__activo
    
    # Métodos
    def desactivar(self):
        self.__activo = False
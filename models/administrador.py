from .usuario import Usuario

class Administrador(Usuario):
    def __init__(self, codigo, nombre, apellido, numero, correo):
        super().__init__(codigo, nombre, apellido, numero, correo);
        self.__area = 1
        
    # area
    @property
    def area(self):
        return self.__area
    
    @area.setter
    def area(self, area):
        self.__area = area
    
    # Métodos
    def registrar():
        pass

    def eliminar():
        pass

    def editar():
        pass
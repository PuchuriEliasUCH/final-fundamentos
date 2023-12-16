from .usuario import Usuario

class Administrador(Usuario):
    def __init__(self, codigo, nombre, apellido, numero, correo, contra):
        super().__init__(codigo, nombre, apellido, numero, correo);
        self.__contra = contra
        
    # Contraseña     
    @property
    def contra(self):
        return self.__contra
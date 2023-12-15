class Usuario():
    def __init__(self, codigo, nombre, apellido, numero, correo):
        self.__codigo = codigo
        self.__nombre = nombre.title()
        self.__apellido = apellido.title()
        self.__numero = numero
        self.__correo = correo
        self.__activo = True
    
    # Nombre
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre  
    
    # Apellido
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
      
    # Número
    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
      
    # correo
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, correo):
        self.__correo = correo

    # activo
    @property
    def activo(self):
        return self.__activo
    
    @activo.setter
    def activo(self, activo):
        self.__activo = activo
        
    


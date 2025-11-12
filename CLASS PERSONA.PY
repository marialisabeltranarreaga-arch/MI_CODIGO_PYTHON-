class Persona:
    '''
    Clase que permite crear un objeto de tipo Persona
    '''
    def __init__(self, cedula:str, nombre:str, email:str, genero:str = None
                 , ocupacion:str = None, edad:int = None):
        self._cedula = cedula
        self._email = email
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion
        self._edad = edad
        self._activo = True

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        self._cedula = nueva_cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nueva_nombre):
        self._nombre = nueva_nombre

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nueva_email):
        self._email = nueva_email

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, nueva_genero):
        self._genero = nueva_genero

    @property
    def ocupacion(self):
        return self._ocupacion

    @ocupacion.setter
    def ocupacion(self, nueva_ocupacion):
        self._ocupacion = nueva_ocupacion

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def activo(self):
        return self._activo

    def inactivar_persona(self):
        self._activo = False

    def __str__(self):
        return f'Persona: {self.__dict__.__str__()}'


class Cliente(Persona):
    '''
    Clase que permite crear un objeto de tipo Cliente que hereda de Persona
    '''
    def __init__(self, cedula: str, nombre: str, email: str, 
                 genero: str = None, ocupacion: str = None, 
                 edad: int = None, categoria: str = "Regular", 
                 numero_cliente: str = None):
        
        # Llamar al constructor de la clase padre (Persona)
        super().__init__(cedula, nombre, email, genero, ocupacion, edad)
        
        # Atributos específicos de Cliente
        self._categoria = categoria
        self._numero_cliente = numero_cliente
        self._puntos_fidelidad = 0

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria):
        self._categoria = nueva_categoria

    @property
    def numero_cliente(self):
        return self._numero_cliente

    @numero_cliente.setter
    def numero_cliente(self, nuevo_numero):
        self._numero_cliente = nuevo_numero

    @property
    def puntos_fidelidad(self):
        return self._puntos_fidelidad

    def agregar_puntos(self, puntos: int):
        """Método para agregar puntos de fidelidad al cliente"""
        if puntos > 0:
            self._puntos_fidelidad += puntos
            return f"Se agregaron {puntos} puntos. Total: {self._puntos_fidelidad}"
        else:
            return "Los puntos deben ser un número positivo"

    def canjear_puntos(self, puntos: int):
        """Método para canjear puntos de fidelidad"""
        if puntos <= 0:
            return "Los puntos a canjear deben ser positivos"
        elif puntos > self._puntos_fidelidad:
            return f"Puntos insuficientes. Tienes {self._puntos_fidelidad} puntos"
        else:
            self._puntos_fidelidad -= puntos
            return f"Puntos canjeados: {puntos}. Puntos restantes: {self._puntos_fidelidad}"

    def actualizar_categoria(self):
        """Método para actualizar la categoría basado en puntos"""
        if self._puntos_fidelidad >= 1000:
            self._categoria = "Premium"
        elif self._puntos_fidelidad >= 500:
            self._categoria = "Gold"
        elif self._puntos_fidelidad >= 100:
            self._categoria = "Silver"
        else:
            self._categoria = "Regular"

    def __str__(self):
        return (f'Cliente: {{'
                f'"cedula": "{self.cedula}", '
                f'"nombre": "{self.nombre}", '
                f'"email": "{self.email}", '
                f'"categoria": "{self.categoria}", '
                f'"numero_cliente": "{self.numero_cliente}", '
                f'"puntos_fidelidad": {self.puntos_fidelidad}, '
                f'"activo": {self.activo}'
                f'}}')


if __name__ == '__main__':
    # Probando la clase Persona
    print("=== PRUEBAS DE CLASE PERSONA ===")
    objPersona1 = Persona(cedula='0952830826', nombre='Marialis Beltrán ', email='mbeltrán@mail.com')
    print(objPersona1.cedula)
    objPersona1.cedula = '0952830826'
    print(objPersona1.cedula)
    objPersona1.inactivar_persona()
    print(f"Activo: {objPersona1.activo}")
    print(objPersona1)
    
    print("\n" + "="*50 + "\n")
    
    # Probando la clase Cliente
    print("=== PRUEBAS DE CLASE CLIENTE ===")
    
    # Crear un cliente
    cliente1 = Cliente(
        cedula='0912837853', 
        nombre='Reyyan yildiz', 
        email='reyyan.yildiz@mail.com',
        genero='f',
        ocupacion='licenciada',
        edad=25,
        categoria='Silver',
        numero_cliente='CLI-012'
    )
    
    print(f"Cédula: {cliente1.cedula}")
    print(f"Nombre: {cliente1.nombre}")
    print(f"Email: {cliente1.email}")
    print(f"Categoría: {cliente1.categoria}")
    print(f"Número de cliente: {cliente1.numero_cliente}")
    print(f"Puntos de fidelidad: {cliente1.puntos_fidelidad}")
    print(f"Activo: {cliente1.activo}")
    
    print("\n--- Probando métodos específicos de Cliente ---")
    
    # Agregar puntos
    print(cliente1.agregar_puntos(300))
    cliente1.actualizar_categoria()
    print(f"Nueva categoría: {cliente1.categoria}")
    
    # Agregar más puntos
    print(cliente1.agregar_puntos(400))
    cliente1.actualizar_categoria()
    print(f"Nueva categoría: {cliente1.categoria}")
    
    # Canjear puntos
    print(cliente1.canjear_puntos(200))
    print(f"Puntos después de canje: {cliente1.puntos_fidelidad}")
    
    # Probando el método __str__
    print("\n--- Representación del cliente ---")
    print(cliente1)
    
    print("\n" + "="*50 + "\n")
    
    # Crear otro cliente con valores por defecto
    print("=== SEGUNDO CLIENTE (valores por defecto) ===")
    cliente2 = Cliente(
        cedula='0987654321', 
        nombre='Carlos López', 
        email='carlos.lopez@mail.com'
    )
    
    print(f"Cédula: {cliente2.cedula}")
    print(f"Nombre: {cliente2.nombre}")
    print(f"Email: {cliente2.email}")
    print(f"Categoría: {cliente2.categoria}")  # Usará "Regular" por defecto
    print(f"Número de cliente: {cliente2.numero_cliente}")  # None por defecto
    print(f"Puntos de fidelidad: {cliente2.puntos_fidelidad}")  # 0 por defecto
    
    print("\n--- Agregando puntos al segundo cliente ---")
    print(cliente2.agregar_puntos(1200))
    cliente2.actualizar_categoria()
    print(f"Categoría actualizada: {cliente2.categoria}")
    
    print("\n--- Representación del segundo cliente ---")
    print(cliente2)
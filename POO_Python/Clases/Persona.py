class Persona:
    
    supervisor = ""
    
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.id = 1234
        
    def MostrarInformacion(self):
        print("Informacion de Persona")
        print(f"Id Persona: {self.id}")
        print(f"Nombre Persona: {self.nombre}")
        print(f"Apellido Persona: {self.nombre}")
        print(f"DNI Persona: {self.dni}")
        
class Empleado(Persona):
    def __init__(self, nombre, apellido, dni, cargo, salario):
        super().__init__(nombre, apellido, dni)
        self.cargo = cargo
        self.salario = salario
        
    def MostrarInformacion(self):
        print("Informacion de Empleado")
        print(f"Informacion Añadida a {self.nombre} tiene un cargo en {self.cargo}")
        print(f"Informacion Añadida a {self.nombre} tiene un salario de {self.salario}")
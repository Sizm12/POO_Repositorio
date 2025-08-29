from Clases.Persona import Persona, Empleado

def main():
    persona1 = Persona("Leo", "Alvarez", "042-060917-1000A")
    
    persona1.MostrarInformacion()
    
    empleado = Empleado("Omar", "Robleto", "042-060917-1000D", "Asesor", 2300)
    
    empleado.MostrarInformacion()
    
if __name__ == "__main__":
    main()
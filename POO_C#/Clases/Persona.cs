public class Persona
{
    public Persona() { }

    private Guid Id { get; set; }
    public string Nombre { get; set; }
    public string Apellido { get; set; }
    public string DNI { get; set; }

    public void CrearPersona()
    {
        this.Id = this.CrearIdentificador();
        this.Nombre = "Nombre";
        this.Apellido = "Apellido";
        this.DNI = "DNI";

        Console.ReadLine();
        this.MostrarDatos();
    }

    private void MostrarDatos()
    {
        Console.WriteLine("Identificador de Persona: "+ this.Id);
        Console.WriteLine("NOmbre Persona: "+ this.Nombre);
        Console.WriteLine("Apellido Persona: "+ this.Apellido);
        Console.WriteLine("DNI Persona: "+ this.DNI);
        Console.ReadLine();
    }

    private Guid CrearIdentificador()
    {
        return Guid.NewGuid();
    }
}
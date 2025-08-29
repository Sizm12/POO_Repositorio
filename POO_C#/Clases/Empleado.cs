public class Empleado : Persona
{
    public string CargoTrabajo { get; set; }
    public Guid IdentificadorTrabajo  { get; set; }


    public void LeerInformacion()
    {
        CrearPersona();
        this.IdentificadorTrabajo = Guid.NewGuid();
        Console.WriteLine("{0}", IdentificadorTrabajo);

    }
}
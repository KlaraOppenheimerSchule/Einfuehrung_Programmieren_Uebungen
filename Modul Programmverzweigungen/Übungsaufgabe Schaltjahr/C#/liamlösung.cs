using System.Runtime.CompilerServices;

internal class Program
{
    public static void Main(string[] args)
    {
        Console.WriteLine("Gib hier eine Jahreszahl ein: ");
        string strInput = Console.ReadLine();
        if (strInput != null)
        {
            if (Int32.TryParse(strInput, out var intInput))
            {
                var objConvert = new PunktZuNote(intInput);
            }
        }
    }
}

class PunktZuNote
{
    private int intJahreszahl;

    public PunktZuNote(int intJahreszahl)
    {
        this.intJahreszahl = intJahreszahl;
        PrüfeObSchaltjahr();
    }

    private void PrüfeObSchaltjahr()
    {
        if ((intJahreszahl % 4 == 0 && intJahreszahl % 100 != 0) || intJahreszahl % 400 == 0)
        {
            Console.WriteLine(intJahreszahl + " ist ein Schaltjahr.");
        }
        else
        {
            Console.WriteLine(intJahreszahl + " ist kein Schaltjahr.");
        }
    }
}
Console.WriteLine("Gib die erste Zahl an.");
int eingabe1 = int.Parse(Console.ReadLine());
Console.WriteLine("Gib die zweite Zahl an.");
int eingabe2 = int.Parse(Console.ReadLine());

if (eingabe1 > eingabe2)
{
    Console.WriteLine($"Der größte gemeinsame Teiler der beiden Zahlen {eingabe1} und {eingabe2} ist {getGGT(eingabe2, eingabe1)}");
}
else
{
    Console.WriteLine($"Der größte gemeinsame Teiler der beiden Zahlen {eingabe1} und {eingabe2} ist {getGGT(eingabe1, eingabe2)}");
}

int getGGT(int zahl1, int zahl2)
{
    if (zahl1 == zahl2 || zahl2 == 0)
    {
        return zahl1;
    }
    else
    {
        return getGGT(zahl2, zahl1 % zahl2);
    }
}
Console.WriteLine("Gib die Länge deiner Fibonacci-Reihenfolge an.");
int anzahl = int.Parse(Console.ReadLine());
int fiboZahl = 1;
List<int> fiboReihenfolge = new List<int>() { 1 };
getNextFibo(anzahl, fiboZahl);

Console.WriteLine("Die Fibonacci-Reihenfolge ist:");
foreach (var item in fiboReihenfolge)
{
    Console.WriteLine($"{item}");
}

void getNextFibo(int anzahl, int letzteZahl)
{
    if (fiboReihenfolge.Count == anzahl)
    {
        return;
    }
    fiboReihenfolge.Add(fiboZahl);
    fiboZahl = fiboZahl + letzteZahl;
    getNextFibo(anzahl, fiboZahl);

}
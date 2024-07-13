using Uebung_Schaltjahr_JG;

while (true)
{
Console.WriteLine("Enter a year, if you want to know if it is a leap year.");

Year currentYear = new Year(Console.ReadLine());

Console.WriteLine(currentYear.Output);
}

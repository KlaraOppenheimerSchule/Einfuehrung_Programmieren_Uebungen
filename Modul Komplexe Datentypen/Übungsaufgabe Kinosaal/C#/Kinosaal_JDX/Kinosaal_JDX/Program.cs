using Kinosaal_JDX;

Array Kinosaal = new char[4, 5];
System.Random r = new System.Random();

// Fills with empty seats
for (int i = 0; i < 5; i++)
{
    for (int j = 0; j < 4; j++)
    {
        Kinosaal.SetValue('0', j, i);
    }
}

Logic l = new Logic();
l.open(Kinosaal);
l.Plan(Kinosaal);

Console.WriteLine();
Console.WriteLine("Please enter where youd like to reserve a seat");
Console.WriteLine("Form: [Row], [Column]");

Boolean readoperation = true;
while (readoperation)
{
    string input = Console.ReadLine();

    if (!input.Contains(','))
    {
        Console.WriteLine("Please enter a valid response");
    }
    else
    {
        char reservation = (char) Kinosaal.GetValue(int.Parse(input.Substring(0, input.IndexOf(','))), int.Parse(input.Substring(input.IndexOf(',') + 1)));
        if (reservation == '1')
        {
            Console.WriteLine("Seat already Reserved! Try another!");
        }
        else
        {
            Kinosaal.SetValue('X', int.Parse(input.Substring(0, input.IndexOf(','))), int.Parse(input.Substring(input.IndexOf(',') + 1)));
            readoperation = false;
        }
    }
}

l.Plan(Kinosaal);
l.save(Kinosaal);

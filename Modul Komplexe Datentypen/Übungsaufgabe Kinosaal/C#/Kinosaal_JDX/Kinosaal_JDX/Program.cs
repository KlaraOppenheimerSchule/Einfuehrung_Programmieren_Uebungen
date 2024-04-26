using Kinosaal_JDX;

Array Kinosaal = new char[4, 5];
//Kinosaal.Initialize();
//char reserved = '1';
System.Random r = new System.Random();
for (int i = 0; i < 5; i++)
{
    for (int j = 0; j < 4; j++)
    {
        Kinosaal.SetValue('0', j, i);
    }
}

//for (int i = 0; i < 4; i++)
//{
//    Kinosaal.SetValue(reserved, r.Next(4), r.Next(5));
//}

Logic l = new Logic();
l.open(Kinosaal);
l.Plan(Kinosaal);
//for (int l = 0; l < 5; l++)
//{
//    for (int k = 0; k < 4; k++)
//    {
//        Console.Write(" |" + Kinosaal.GetValue(k, l) + "| ");
//    }
//    Console.WriteLine();
//}
Console.WriteLine();
Console.WriteLine("Please enter where youd like to reserve a seat");
Console.WriteLine("Form: [Roow], [Column]");
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

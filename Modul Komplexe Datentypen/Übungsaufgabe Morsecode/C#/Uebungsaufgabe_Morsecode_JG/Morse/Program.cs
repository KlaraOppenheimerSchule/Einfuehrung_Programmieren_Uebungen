using System;

Dictionary<string, string> _morseZeichen = new()
{
    { "A", ".-" },
    { "B", "-..." },
    { "C", "-.-." },
    { "D", "-.." },
    { "E", "." },
    { "F", "..-." },
    { "G", "--." },
    { "H", "...." },
    { "I", ".." },
    { "J", ".---" },
    { "K", "-.-" },
    { "L", ".-.." },
    { "M", "--" },
    { "N", "-." },
    { "O", "---" },
    { "P", ".--." },
    { "Q", "--.-" },
    { "R", ".-." },
    { "S", "..." },
    { "T", "-" },
    { "U", "..-" },
    { "V", "...-" },
    { "W", ".--" },
    { "X", "-..-" },
    { "Y", "-.--" },
    { "Z", "--.." },
    { "0", "-----" },
    { "1", ".----" },
    { "2", "..---" },
    { "3", "...--" },
    { "4", "....-" },
    { "5", "....." },
    { "6", "-...." },
    { "7", "--..." },
    { "8", "---.." },
    { "9", "----." },
};

Console.WriteLine("Bitte gib einen Buchstaben, ein Wort oder einen Satz ein.");
string? eingabe = Console.ReadLine();

while (eingabe == null)
{
    Console.WriteLine("Ungültige Eingabe.");
    Console.WriteLine("Bitte gib einen Buchstaben, ein Wort oder einen Satz ein.");
    eingabe = Console.ReadLine();
}

try
{
    for (int i = 0; i < eingabe.Length; i++)
    {
        var check = _morseZeichen[eingabe[i].ToString()];
    }
}
catch (Exception)
{
    Console.WriteLine("Es dürfen keine Sonder- oder Satzzeichen eingegeben werden.");
    Console.WriteLine("Bitte gib einen Buchstaben, ein Wort oder einen Satz ein.");
    eingabe = Console.ReadLine();
}

eingabe = eingabe.ToUpper();

if (eingabe.Length == 1)
{
    Console.WriteLine($"Der Buchstabe {eingabe} entspricht dem Morsezeichen \'{_morseZeichen[eingabe]}\'");
}
else if (eingabe.Contains(" "))
{
    string? morseWord = new("");
    for (int i = 0; i < eingabe.Length; i++)
    {
        if (eingabe[i].ToString() == " ")
        {
            morseWord += " ";
        }
        else
        {
            morseWord += $"\'{_morseZeichen[eingabe[i].ToString()]}\'";
        }
    }
    Console.WriteLine($"Der Satz {eingabe} entspricht den Morsezeichen {morseWord}");
}
else
{
    string? morseWord = new("");
    for (int i = 0; i < eingabe.Length; i++)
    {
        morseWord += $"\'{_morseZeichen[eingabe[i].ToString()]}\'";
    }
    Console.WriteLine($"Das Wort {eingabe} entspricht den Morsezeichen {morseWord}");
}


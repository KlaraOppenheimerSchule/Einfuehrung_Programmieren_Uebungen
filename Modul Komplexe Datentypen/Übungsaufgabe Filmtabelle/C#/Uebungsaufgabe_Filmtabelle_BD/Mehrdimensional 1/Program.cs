using System;

namespace Mehrdimensional_1
{
    class Program
    {
        static void Main(string[] args)
        {
            string[,] zweiDimensionalerArray = new string[4, 4] { { "1", "2", "3", "4" }, { "Es Weihnachtet Schwer", "Bart wird ein Genie", "Der Versager", "Eine ganz normale Familie" }, { "Simpsons Roasting on an Open Fire", "Bart the Genius", "Homer´s Odyssey", "There´s No Disgrace Like Home" }, { "6.12.1991", "20.09.1991", "11.10.1991", "13.09.1991" } };

            int n = 0;
            while (n < 4)
            {
                Console.WriteLine(zweiDimensionalerArray[0, n] + " " + zweiDimensionalerArray[1, n] + " " + zweiDimensionalerArray[2, n] + " " + zweiDimensionalerArray[3, n]);
                n++;
            }
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lotto
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rand = new Random();
            int[] lotto = new int[6];

            for(int i = 0; i < 6; i++)
            {
                lotto[i] = rand.Next(1, 49);
                if (Gleichheit(lotto, i))
                {
                    do
                    {
                        lotto[i] = rand.Next(1, 49);
                    } while (Gleichheit(lotto, i));
                }
                
                Console.WriteLine(lotto[i]);
            }
            Console.ReadKey();
            int[] user = new int[6];
            for(int j = 0; j < 6; j++)
            {
                Console.WriteLine("Bitte geben sie ihre Zahl ein:");
                user[j] = Int32.Parse(Console.ReadLine());
            }
            Console.ReadKey();
        }

        public static bool Gleichheit(int[] array, int i)
        {
            bool pruefung = false;
            for(int k = 0; k < i; k++)
            {
                if (array[i] == array[k])
                {
                    pruefung = true;
                    
                }
                pruefung= false;
            }
            return pruefung;
        }
    }
}

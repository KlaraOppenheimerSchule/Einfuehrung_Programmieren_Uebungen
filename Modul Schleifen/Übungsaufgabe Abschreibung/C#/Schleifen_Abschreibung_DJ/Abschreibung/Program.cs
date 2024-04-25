using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Abschreibung
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Please Input the Cost of the Item");
            float cost = float.Parse(Console.ReadLine());
            Console.WriteLine("Please Input the Time to be calculated for");
            int time = int.Parse(Console.ReadLine());
            float divident;
            divident = cost / time;

            Console.WriteLine("Year \t start \t\t\t removed \t\t\t remaining\n");
            for (int i = 0; i < time; i++) 
            {
                Console.Write(i + " \t");
                Console.Write(cost + " \t\t\t");
                Console.Write(divident + " \t\t\t");
                try 
                {
                    cost = cost - divident;
                    if (cost < 0) 
                    {
                        cost = 0;
                        i = time + 1;
                    }
                }
                catch 
                {
                }
                Console.WriteLine(cost);

            }
            Console.ReadLine();
        }
    }
}

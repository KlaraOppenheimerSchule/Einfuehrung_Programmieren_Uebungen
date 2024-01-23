using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace PinCode
{
    class Program
    {
        static void Main(string[] args)
        {
            PinCodeEach();
        }

        public static void PinCodeFor()
        {
            Random rng = new Random();
            Console.Write("Number of Pins requested:");
            string input = Console.ReadLine();
            int NumRequested = Int32.Parse(input);

            for (int i = 1; i < NumRequested + 1; i++)
            {
                for (int j = 1; j < 5; j++)
                {
                    int random = 0;
                    Task.Delay(2000);
                    random = rng.Next(9);
                    Console.Write(random);
                }
                Console.WriteLine();

            }
            Console.WriteLine("Operation finished");
            Console.ReadLine();
        }

        public static void PinCodeEach()
        {
            Random rng = new Random();
            Console.WriteLine("Number of Pins Required:");
            string input = Console.ReadLine();
            Int32 NumRequested = Int32.Parse(input);
            List<string> pins = new List<string>();
            for (int i = 0; i < NumRequested; i++) 
            {
                string pin = "";
                for (int j = 1; j < 5; j++)
                {
                    pin += rng.Next(9).ToString();
                }
                pins.Add(pin);
            }

            foreach (var item in pins) 
            {
                Console.WriteLine(item);
            }
            Console.ReadLine();
        }
    }
}

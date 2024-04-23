using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ueungsaufgabe_Schaltjahr_JD
{
    class Program
    {
        public static void Main(string[] args)
        {
            int year = 0;
            Boolean isSwitchYear;

            Console.WriteLine("Please enter year to check");
            try
            {
                year = Convert.ToInt32(Console.ReadLine());
            }
            catch(FormatException)
            {
                Console.WriteLine("Something went wrong, type in a Year in Numbers");
                year = Convert.ToInt32(Console.ReadLine());
            }

            Console.WriteLine();
            Console.WriteLine("calculating if Year is Viable");
            isSchaltjahr check = new isSchaltjahr();
            isSwitchYear = check.checkYear(year);

            if (isSwitchYear)
            {
                Console.WriteLine();
                Console.WriteLine("The Year " + year + " is a viable Year!");
                Console.WriteLine("Do you want to Check again?: [Y]es [N]o");
            }
            else 
            {
                Console.WriteLine();
                Console.WriteLine("The Year " + year + " is not a viable Year!");
                Console.WriteLine("Do you want to Check again?: [Y]es [N]o");
            }
            
            if (Console.ReadKey().Key == ConsoleKey.Y) 
            {
                Console.WriteLine();
                Main(args);
            }
            
        }
    }

    public class isSchaltjahr
    {
        public Boolean checkYear(int param)
        {
            bool switchYear = false;

            //Check if Year is Set
            if( param != 0)
            {
                //check if year is dividable by 4 and 100
                if (param % 4 == 0 && param % 100 != 0)
                {
                    switchYear = true;
                }
                else 
                {
                    //check if year is dividable by 400
                    if (param % 400 == 0) 
                    {
                        switchYear = true;
                    }
                }
            }

            return switchYear;
        }
    }
}

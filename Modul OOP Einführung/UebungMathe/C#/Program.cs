using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UebungMathe
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Math mathobj = new Math();
            Console.WriteLine(mathobj.sum(3, 4));
            Console.WriteLine(mathobj.square(3));
            Console.WriteLine(mathobj.fac(3));
            Console.WriteLine(mathobj.facrec(3));
            Console.ReadLine();
        }
    }
}

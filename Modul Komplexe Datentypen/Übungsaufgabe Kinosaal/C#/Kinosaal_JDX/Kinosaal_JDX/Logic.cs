using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Kinosaal_JDX
{
    public class Logic
    {
        public void Plan(Array _array)
        {
            for (int l = 0; l < 5; l++)
            {
                for (int k = 0; k < 4; k++)
                {
                    Console.Write(" |" + _array.GetValue(k, l) + "| ");
                }
                Console.WriteLine();
            }
        }

        public void save(Array _array)
        {
            FileStream stream = System.IO.File.OpenWrite("C:\\Users\\jadre\\OneDrive\\Dokumente\\kinosaal.txt");
            using (stream)
            {
                StreamWriter writer = new StreamWriter(stream);
                for (int l = 0; l < 5; l++)
                {
                    for (int k = 0; k < 4; k++)
                    {
                        writer.WriteLine(k + "," + l + "," + _array.GetValue(k, l));
                    }
                }
                writer.Flush();
            }

        }

        public Array open(Array _array)
        {


            FileStream stream = File.OpenRead("C:\\Users\\jadre\\OneDrive\\Dokumente\\kinosaal.txt");
            using (stream)
            {
                StreamReader reader = new StreamReader(stream);
                while (!reader.EndOfStream)
                {
                    try
                    {
                        string current = reader.ReadLine();
                        int k = int.Parse(current.Substring(0, 1));
                        int l = int.Parse(current.Substring(2, 1));
                        char value = char.Parse(current.Substring(4, 1));
                        _array.SetValue(value, k, l);
                    }
                    catch (System.ArgumentOutOfRangeException)
                    {
                        Console.WriteLine("Loading has finished");
                    }
                }
            }

            return _array;

        }
    }
}

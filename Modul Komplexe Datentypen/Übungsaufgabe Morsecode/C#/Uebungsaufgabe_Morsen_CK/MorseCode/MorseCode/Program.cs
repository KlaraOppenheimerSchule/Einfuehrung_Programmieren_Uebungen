using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace MorseCode
{
    class Program
    {
        static void Main(string[] args)
        {
            Dictionary<char,string> morsen = new Dictionary<char, string>();
            InitializeDictionary(morsen);
            Console.WriteLine("Schreiben Sie etwas:");
            string eingabe = Console.ReadLine();
            string geingabe = eingabe.ToUpper();
            for (int i = 0; i < geingabe.Length; i++)
            {
                if (i > 0)
                    Console.Write('/');

                char c = geingabe[i];
                if (morsen.ContainsKey(c))
                    Console.Write(morsen[c]);
            }

            Console.WriteLine();
            Console.ReadKey();
        }

        public static void InitializeDictionary(Dictionary<char,string> meinDict)
        {
            meinDict.Add('A', ".-");
            meinDict.Add('B', "-...");
            meinDict.Add('C', "-.-.");
            meinDict.Add('D', "-..");
            meinDict.Add('E', ".");
            meinDict.Add('F', "..-.");
            meinDict.Add('G', "--.");
            meinDict.Add('H', "....");
            meinDict.Add('I', "..");
            meinDict.Add('J', ".---");
            meinDict.Add('K', "-.-");
            meinDict.Add('L', ".-..");
            meinDict.Add('M', "--");
            meinDict.Add('N', "-.");
            meinDict.Add('O', "---");
            meinDict.Add('P', ".--.");
            meinDict.Add('Q', "--.-");
            meinDict.Add('S', "...");
            meinDict.Add('T', "-");
            meinDict.Add('U', "..-");
            meinDict.Add('V', "...-");
            meinDict.Add('W', ".--");
            meinDict.Add('X', "-..-");
            meinDict.Add('Y', "-.--");
            meinDict.Add('Z', "--..");
            meinDict.Add('0', "-----");
            meinDict.Add('1', ".----");
            meinDict.Add('2', "..---");
            meinDict.Add('3', "...--");
            meinDict.Add('4', "....-");
            meinDict.Add('5', ".....");
            meinDict.Add('6', "-....");
            meinDict.Add('7', "--...");
            meinDict.Add('8', "---..");
            meinDict.Add('9', "----.");
        }
    }
}

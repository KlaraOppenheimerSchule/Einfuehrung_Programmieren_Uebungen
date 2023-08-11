using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UebungMathe
{
    internal class Math
    {
        public int sum(int a, int b)
        {
            return a + b;
        }

        public int square(int a)
        {
            return a * a;
        }

        public bool checkPos(int a)
        {
            return a > 0; //returns true if positive
        }

        public int fac(int a)
        {
            int result = 1;
            for (int i = 1; i <= a; i++)
            {
                result = result*i;
            }
            return result;
        }

        public int facrec(int a)
        {
            if (a == 1)
            {
                return 1;
            }
            else
            {
                return a * facrec(a - 1);
            }
        }

    }
}

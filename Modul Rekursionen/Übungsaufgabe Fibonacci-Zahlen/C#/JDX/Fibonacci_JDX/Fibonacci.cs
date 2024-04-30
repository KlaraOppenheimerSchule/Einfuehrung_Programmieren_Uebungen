using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace Fibonacci_JDX
{
    /// <summary>
    /// Fibonacci Class for KOS Recursive Training
    /// </summary>
    public class Fibonacci
    {
        /// <summary>
        /// Finds the n-th Fibonacci Number
        /// </summary>
        /// <param name="i"> The Nth Number to be calculated</param>
        /// <returns>The corresponding Fibonacci Sequence Number</returns>
        public int Fibo(int i)
        {
            int ret = 0;
            if (i == 0) ret = 0;
            if (i == 1) ret = 1;
            if (i > 1) 
            {
                ret = Fibo(i - 1) + Fibo(i - 2);
            }

            return ret;
        }
    }
}

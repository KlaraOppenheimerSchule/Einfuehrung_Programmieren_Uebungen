using Fibonacci_JDX;


Console.WriteLine("Enter the Nth Fibonacci Number");
int i = int.Parse(Console.ReadLine());
Fibonacci fib = new Fibonacci();
Console.WriteLine(fib.Fibo(i).ToString());


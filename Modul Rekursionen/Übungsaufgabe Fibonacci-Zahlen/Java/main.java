import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Geben Sie eine Zahl n ein, um die Fibonacci-Reihe zu berechnen: ");
        int n = input.nextInt();

        System.out.print("Fibonacci-Reihe für " + n + ": ");
        for (int i = 0; i < n; i++) {
            System.out.print(fib(i) + ", ");
        }
    }
    public static int fib(int n) {
        if (n <= 1) {
            return n;
        } else {
            return fib(n - 1) + fib(n - 2);
        }
    }
}

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Geben Sie eine Zahl n ein, um die 20er Potenz zu berechnen: ");
        int n = input.nextInt();

        System.out.print("20er Potenz mit " + n + ": ");
        System.out.print(power(n));

    }
    public static long power(int n) {
        if (n == 0) {
            return 1;
        }
        return 20 * power(n - 1);
    }
}

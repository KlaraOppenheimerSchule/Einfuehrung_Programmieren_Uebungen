public class GCD_recursive {
    // explore recursive the greatest common divisor using the euclidean algorithm
    public static int gcd (int a, int b){
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }

    public static void main(String[] args) {
        System.out.println(gcd(18, 12));
    }
}
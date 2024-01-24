public class Main
{
    public static void main(String[] args) {
        int[] normal = new int[10];
        normal[0] = 0;
        normal[1] = 1;
        normal[2] = 2;
        normal[3] = 3;
        normal[4] = 4;
        normal[5] = 5;
        normal[6] = 6;
        normal[7] = 7;
        normal[8] = 8;
        normal[9] = 9;

        reverse(normal);
}

    static void reverse(int[] initialArray)
    {
        int[] reversedArray = new int[10];
        int j = 10;
        for (int i = 0; i < 10; i++) {
            reversedArray[j-1] = initialArray[i];
            System.out.println(reversedArray[j-1]);
            j--;
        }
    }
}

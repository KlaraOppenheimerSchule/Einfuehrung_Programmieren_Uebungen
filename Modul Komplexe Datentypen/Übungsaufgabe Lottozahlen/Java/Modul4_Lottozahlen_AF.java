import java.util.Arrays;
import java.util.Scanner;

public class Main
{
    public static void main(String[] args)
    {
        //Array für die gezogenen Zahlen
        int[] drawnNumbers = new int[6];

        //Zufällige Lottozahlen generieren
        for (int i = 0; i < 6; i++) {
            drawnNumbers[i] = generateRandomNumbers();
        }

        //Array für die vom Spieler ausgewählten Zahlen
        int[] guessedNumbers = new int[6];

        //Spieler nach Zahlen fragen
        Scanner scanner = new Scanner(System.in);
        System.out.println("Geben Sie Ihre sechs Zahlen zwischen 1 und 49 ein:");

        for (int i = 0; i < 6;) {
            System.out.print("Zahl " + (i + 1) + ": ");
            int scannedInt = scanner.nextInt();
            if (scannedInt>= 1 && scannedInt<= 49){
                guessedNumbers[i] = scannedInt;
                i++;
            }
            else
            {
                System.out.println("Bitte geben Sie nur Zahlen zwischen 1 und 49 ein!");
            }

        }
        // Lottozahlen und Spielerzahlen ausgeben
        System.out.println("Gezogene Zahlen: " + Arrays.toString(drawnNumbers));
        System.out.println("Ihre Zahlen:     " + Arrays.toString(guessedNumbers));
    }

    //Methode zur Generation einer Zufallszahl zwischen 1 und 49
    private static int generateRandomNumbers()
    {
        return (int) (Math.random() * 49)+1;
    }
}

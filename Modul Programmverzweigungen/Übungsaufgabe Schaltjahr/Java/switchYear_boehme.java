import java.util.Scanner;

public class SwitchYear {

    public static boolean isSwitchYear(int year) {
        boolean isSwitchYear = false;
        isSwitchYear = year % 400 == 0 || (year % 100 != 0 && year % 4 == 0);
        return isSwitchYear;
    }

    /**
     * Runs from a given start Year to a given end Year and prints to console only the switch Years.
     * @param startYear should be positive
     * @param endYear should be positive
     */
    public static void iterateOverYears(int startYear, int endYear) {
        for (int i = startYear; i < endYear; i++) {
            if (isSwitchYear(i)) {
                System.out.println("The Year " + i + " is a switch Year.");
            }
        }
    }

    public static void main(String[] args) {
        // create scanner obj to read from console inputs
        Scanner scanner = new Scanner(System.in);

        /*
        iterateOverYears(111, 2300);
        */

        while (true) {

            System.out.print("Enter a Year: ");
            
            // Check if the next input is an integer
            if (scanner.hasNextInt()) {
                // If it's an integer, read and store the value
                int userInput = scanner.nextInt();

                if (isSwitchYear(userInput)) {
                    System.out.println("The Year " + userInput + " is a switch year.");
                } else {
                    System.out.println("The Year " + userInput + " is not a switch year.");
                }
            } else {
                // If it's not an integer, display an error message
                System.out.println("Error: Please enter a valid integer.");
            }
        }
    }
}

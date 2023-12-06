public class SwitchYear {

    public static boolean isSwitchYear(int year) {
        boolean isSwitchYear = false;
        isSwitchYear = year % 400 == 0 || (year % 100 != 0 && year % 4 == 0);
        return isSwitchYear;
    }

    public static void main(String[] args) {
        int startYear = 400;
        int endYear = 2300;

        for (int i = startYear; i < endYear; i++) {
            if (isSwitchYear(i)) {
                System.out.println("The Year " + i + " is a switch Year.");
            }
        }
    }
}

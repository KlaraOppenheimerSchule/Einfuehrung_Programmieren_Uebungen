import java.util.Scanner;

class GradeConverter
{
    private static double convertPointsToGrades(int punkte) {
        if ( punkte == 100) {
            return 1.0;
        } else if (punkte == 99 || punkte == 98) {
            return 1.1;
        } else if (punkte == 97 || punkte == 96) {
            return 1.2;
        } else if (punkte == 95 || punkte == 94) {
            return 1.3;
        } else if (punkte == 93 || punkte == 92) {
            return 1.4;
        } else if (punkte == 91) {
            return 1.5;
        } else if (punkte == 90) {
            return 1.6;
        }
        else if (punkte == 89)
        {
            return 1.7;
        }
        else if (punkte == 88)
        {
            return 1.8;
        }
        else if (punkte == 87)
        {
            return 1.9;
        }
        else if (punkte == 86|| punkte == 85)
        {
            return 2.0;
        }
        else if (punkte == 84)
        {
            return 2.1;
        }
        else if (punkte == 83)
        {
            return 2.2;
        }
        else if (punkte == 82)
        {
            return 2.1;
        }
        else if (punkte == 81)
        {
            return 2.4;
        }
        else if (punkte == 80)
        {
            return 2.5;
        }
        else if (punkte == 79)
        {
            return 2.6;
        }
        else if (punkte == 78 ||punkte == 77)
        {
            return 2.7;
        }
        else if (punkte == 76)
        {
            return 2.8;
        }
        else if (punkte == 75||punkte == 74)
        {
            return 2.9;
        }
        else if (punkte == 73)
        {
            return 3.0;
        }
        else if (punkte == 72|| punkte == 71)
        {
            return 3.1;
        }
        else if (punkte == 70)
        {
            return 3.2;
        }
        else if (punkte == 69|| punkte == 68)
        {
            return 3.3;
        }
        else if (punkte == 67) {
            return 3.4;
        }
        //else if (punkte == 66)
            //        {
            //            return ?;
            //        }
        else if (punkte == 65)
        {
            return 3.5;
        }
        else if (punkte == 64)
        {
            return 3.6;
        }
        else if (punkte == 63||punkte == 62)
        {
            return 3.7;
        }
        else if (punkte == 61)
        {
            return 3.8;
        }
        else if (punkte == 60||punkte==59)
        {
            return 3.9;
        }
        else if (punkte == 58||punkte==57)
        {
            return 4.0;
        }
        else if (punkte == 56||punkte==55)
        {
            return 4.1;
        }
        else if (punkte == 54)
        {
            return 4.2;
        }
        else if (punkte == 53||punkte == 52)
        {
            return 4.3;
        }
        else if (punkte == 51||punkte==50)
        {
            return 4.4;
        }
        else if (punkte == 49)
        {
            return 4.5;
        }
        else if (punkte == 48||punkte==47)
        {
            return 4.6;
        }
        else if (punkte == 46||punkte==45)
        {
            return 4.7;
        }
        else if (punkte == 44||punkte==43)
        {
            return 4.8;
        }
        else if (punkte == 42||punkte==41)
        {
            return 4.9;
        }
        else if (punkte == 40||punkte==39||punkte==38)
        {
            return 5.0;
        }
        else if (punkte == 37||punkte==36)
        {
            return 5.1;
        }
        else if (punkte == 35||punkte==34)
        {
            return 5.2;
        }
        else if (punkte == 33||punkte==32)
        {
            return 5.3;
        }
        else if (punkte == 31||punkte==30)
        {
            return 5.4;
        }
        else if (punkte == 29)
        {
            return 5.5;
        }
        else if (punkte < 29 && punkte > 22)
        {
            return 5.6;
        }
        else if (punkte < 23 && punkte > 16)
        {
            return 5.7;
        }
        else if (punkte < 17 && punkte > 11)
        {
            return 5.8;
        }
        else if (punkte < 12 && punkte > 5)
        {
            return 5.9;
        }
        else if (punkte < 6 && punkte >= 0)
        {
            return 6.0;
        }
        return 0;
    }
    public static void main(String[] args) {
        Scanner text = new Scanner(System.in);
        int points;
        System.out.println("Enter Points");

        while (!text.hasNextInt()) {
            System.out.println("Invalid input. Please enter valid points:");
            text.next();
        }

        points = text.nextInt();

        double convertedGrade = convertPointsToGrades(points);
        System.out.println("Input points correspond to grade: " + convertedGrade);
    }
}

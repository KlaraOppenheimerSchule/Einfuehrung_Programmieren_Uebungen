public class Main {
    public static void main(String[] args) {
    String[] bestFriends = new String[3];
    bestFriends[0] = "Hans";
    bestFriends[1] = "Uwe";
    bestFriends [2] = "Hildegard";

    printFriends(bestFriends);
    bestFriends[2] = "";

    printFriends(bestFriends);
    bestFriends[2] = "Uschi";
    
    printFriends(bestFriends);
    }

    public static void  printFriends(String[]friends)
    {
        System.out.println("Meine besten Freunde:");

        for (int i = 0; i < 3; i++)
        {
            System.out.println(friends[i]);
        }
        System.out.println();
    }
}

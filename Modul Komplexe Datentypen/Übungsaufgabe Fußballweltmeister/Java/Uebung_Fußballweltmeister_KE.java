import java.util.*;

public class Fußballweltmeister {

    public static void main(String[] args) {
        Fußballweltmeister myTable = new Fußballweltmeister();
        myTable.createTable();
    }

    public void createTable() {
        Map<String, Integer> myTable = new HashMap<>();
        ArrayList<ArrayList<Integer>> listOfYears = new ArrayList<>();

        listOfYears.add(new ArrayList<>(Arrays.asList(1958, 1962, 1970, 1994, 2002)));
        listOfYears.add(new ArrayList<>(Arrays.asList(1934, 1938, 1982, 2006)));
        listOfYears.add(new ArrayList<>(Arrays.asList(1954, 1974, 1990, 2014)));
        listOfYears.add(new ArrayList<>(Arrays.asList(1930, 1950)));
        listOfYears.add(new ArrayList<>(Arrays.asList(1978, 1986)));
        listOfYears.add(new ArrayList<>(Arrays.asList(1906)));
        listOfYears.add(new ArrayList<>(Arrays.asList(1998)));
        listOfYears.add(new ArrayList<>(Arrays.asList(2010)));

        Map<Map.Entry<String, Integer>, ArrayList<Integer>> myFinalTable = new HashMap<>();
        myTable.put("Brasilien", 5);
        myTable.put("Italien", 4);
        myTable.put("Deutschland", 4);
        myTable.put("Uruguay", 2);
        myTable.put("Argentinien", 2);
        myTable.put("England", 1);
        myTable.put("Frankreich", 1);
        myTable.put("Spanien", 1);

        Iterator<ArrayList<Integer>> yearIterator = listOfYears.iterator();
        Iterator<Map.Entry<String, Integer>> iterator = myTable.entrySet().iterator();

        while(yearIterator.hasNext()) {
            ArrayList<Integer> temp = yearIterator.next();
            myFinalTable.put(iterator.next(), temp);
        }

        myFinalTable.forEach(
                (entry, list) -> System.out.printf("%-20s%-20d%s%n", entry.getKey(), entry.getValue(), list.toString())
        );
    }

}

public class TANKEN{

    private double price;
    private double costsTotal;
    private double costs;
    private double amount;
    private String type;
    private String discount;


    public TANKEN(double a, String t){
        this.amount = a;
        this.type = t;

        costsTotal = calculateTotal(amount, type);

        printCosts();
    }

    private double calculateTotal(double a, String t){

        switch(t){
            case "Super":
                price = 1.80;
                break;
            case "E10":
                price = 1.74;
                break;
            case "Super+":
                price = 1.91;
                break;
        }

        costs = price * a;

        if(costs >= 100){
            costs = costs - costs * 0.05;
            discount = "Sie haben einen Rabatt von 5% erhalten!";
        } else{
            discount = "";
        }

        return costs;
    }

    private void printCosts(){
        System.out.println("Sie haben " + amount + " Liter " + type + " getankt");
        System.out.println("Der preis pro Liter beträgt: " + price);
        System.out.println("Sie haben insgesammt " + costs + " Euro gezahlt. " + discount);
    }
}

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		EncryptDecrypt CrypticObject = new EncryptDecrypt();
		Scanner sc = new Scanner(System.in);
		boolean pruef = false;
		do {
			System.out.println("Wollen sie Entschlüsseln oder Verschlüsseln?(Entschlüsseln=1;Verschlüsseln=2)");
			int auswahl = sc.nextInt();
			sc.nextLine();
			switch (auswahl) {
			case 1:
				System.out.println("Geben Sie die zu entschlüsselnde Nachricht ein: ");
				CrypticObject.setNachricht(sc.nextLine());
				System.out.println("Geben Sie den Schlüssel ein: ");
				CrypticObject.setSchlüssel(sc.nextInt());
				String lösung = CrypticObject.decryptMessage(CrypticObject.getNachricht(), CrypticObject.getSchlüssel());
				System.out.println("Verschlüsselte Nachricht:" + lösung);
				pruef = true;
				break;

			case 2:
				System.out.println("Geben Sie die zu verschlüsselnde Nachricht ein: ");
				CrypticObject.setNachricht(sc.nextLine());
				System.out.println("Geben Sie den Schlüssel ein: ");
				CrypticObject.setSchlüssel(sc.nextInt());
				String lösung2 = CrypticObject.encryptMessage(CrypticObject.getNachricht(), CrypticObject.getSchlüssel());
				System.out.println("Verschlüsselte Nachricht:" + lösung2);
				pruef = true;
				break;
			default:
				System.out.println("Ungültige Eingabe");
				pruef = false;
				break;
			}

		} while (pruef == false);
		sc.close();
	}
}

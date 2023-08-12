
public class EncryptDecrypt {
	String nachricht;
	int schlüssel;

	public int getSchlüssel() {
		return schlüssel;
	}

	public void setSchlüssel(int schlüssel) {
		this.schlüssel = schlüssel;
	}

	public String getNachricht() {
		return nachricht;
	}

	public void setNachricht(String nachricht) {
		this.nachricht = nachricht;
	}

	public EncryptDecrypt() {

	}

	public String encryptMessage(String nachricht, int schlüssel) {
		nachricht = nachricht.replaceAll("\\s", "");
		char[] neu = nachricht.toCharArray();
		for (int i = 0; i < neu.length; i++) {
			char c = neu[i];
			if (Character.isUpperCase(c)) {
				c = (char) ((c - 65 + schlüssel) % 26 + 65);
				neu[i] = c;
			} else if (Character.isLowerCase(c)) {
				c = (char) ((c - 97 + schlüssel) % 26 + 97);
				neu[i] = c;
			}
		}
		String returnValue = new String(neu);
		return returnValue;
	}

	public String decryptMessage(String nachricht, int schlüssel) {
		nachricht = nachricht.replaceAll("\\s", "");
		char[] neu = nachricht.toCharArray();

		for (int i = 0; i < neu.length; i++) {
			char c = neu[i];
			if (Character.isUpperCase(c)) {
				c = (char) ((c - 39 - schlüssel) % 26 + 65);
				neu[i] = c;
			} else if (Character.isLowerCase(c)) {
				c = (char) ((c -71 - schlüssel) % 26 + 97);
				neu[i] = c;
			}
		}
		String returnValue = new String(neu);
		return returnValue;
	}

}
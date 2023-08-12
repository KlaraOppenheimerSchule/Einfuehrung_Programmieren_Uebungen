class morsetrans:
    morse = { "A": ".-", "B": "-...", "C": "-.-.",
          "D": "-..", "E": ".", "F": "..-.",
          "G": "--.", "H": "....", "I": "..",
          "J": ".---", "K": "-.-", "L": ".-..",
          "M": "--", "N": "-.", "O": "---",
          "P": ".--.", "Q": "--.-", "R": ".-.",
          "S": "...", "T": "-", "U": "..-",
          "V": "...-", "W": ".--", "X": "-..-",
          "Y": "-..-", "Z": "--..", "1": ".----",
          "2": "..---", "3": "...--", "4": "....-",
          "5": ".....", "6": "-....", "7": "--...",
          "8": "---..", "9": "----.", "0": "-----"
}
    letter = ""
    def eingabe(self):
        self.letter = input("Bitte geben Sie einen Satz ein:")
        self.letter = self.letter.upper()

    def übersetzung(self):
        for i in range(0, len(self.letter)):
            if self.letter[i] == " ":
                print(" ")
            for key in self.morse:
                if key == self.letter[i]:
                    print(self.morse[key])

morse = morsetrans()
morse.eingabe()
morse.übersetzung()
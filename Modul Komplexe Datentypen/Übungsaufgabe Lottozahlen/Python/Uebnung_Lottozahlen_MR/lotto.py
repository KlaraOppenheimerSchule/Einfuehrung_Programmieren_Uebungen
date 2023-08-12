#TO DO: Vergleich der Zahlen umbauen, gleiche Zahl nicht doppelt

import random
x = 6

class Lottomaschine:
    lottozahlen = []
    tippzettel = []

    def pickRandom(self):

        while len(self.lottozahlen) < x:
            nums = random.randint(1,49)
            self.lottozahlen.append(nums)
    	    
    def zettelFuellen(self):
        while len(self.tippzettel) < x :
            zahl = int(input("Bitte geben Sie eine Zahl ein: "))
            if zahl <= 0 or zahl > 49:
                print("Bitte geben Sie Zahlen von 1-49 ein")
            else:
                self.tippzettel.append(zahl)    

    def ausgabe(self):
        print(self.lottozahlen)
        print(self.tippzettel)

    def vergleicheZahlen(self):
        summe = 0
        for i in range(x):
            if self.lottozahlen[i] == self.tippzettel[i]:
                summe = summe + 1

        if summe == 1:
            print("Sie haben 1 Zahl richtig")
        else:
            print("Sie haben", summe, "Zahlen richtig")
            
lotto = Lottomaschine()

lotto.zettelFuellen()
lotto.pickRandom()
lotto.ausgabe()
lotto.vergleicheZahlen()
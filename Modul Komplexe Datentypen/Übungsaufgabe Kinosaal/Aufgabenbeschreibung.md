# Aufgabe Kinosaal - mehrdimensional

## Schwierigkeitsgrad: ***

## Aufgabenbeschreibung
1. Erstellen Sie für einen Kinosaal ein Reservierungssystem (stark vereinfacht), das es ermöglicht, freie Plätze je nach Kundenwunsch zu reservieren. Da der jetzige Kenntnisstand noch keine Nutzung einer persistenten Quelle vorsieht, werden wir uns vorerst damit begnügen, dass der Nutzer folgenden Ablauf vorfindet: 
		
Nach der Eingabe der gewünschten Reihe sowie der Platznummer wird geprüft, ob der gewünschte Platz aktuell verfügbar ist. Ob ein Platz in dem erstmals kleinen Kinosaal mit drei Reihen und je fünf Plätzen verfügbar ist, kann in einem mehrdimensionalen komplexen Datentyp erkannt werden. 

![Kinosaal](https://github.com/KlaraOppenheimerSchule/Einfuehrung_Programmieren_Uebungen/blob/90f4b89000f2c4e50adf657a0c2d2e1c134a4261/Modul%20Komplexe%20Datentypen/%C3%9Cbungsaufgabe%20Kinosaal/Kinosaal.jpg)

Sofern ein Platz frei ist, wird 1 für true eingetragen, falls der Platz belegt ist, wird 0 für false eingetragen. Der Nutzer erhält nach der Überprüfung des Reservierungswunsches eine entsprechende Rückmeldung.

2. Das Eintragen von 0 oder 1 beim Anlegen des komplexeden Datentyps soll nun nicht mehr manuell vom Programmierer erfolgen, sondern mit Hilfe einer Zufallsfunktion erfolgen. Sicherlich finden Sie eine passende Methode in der Programmiersprache Ihrer Wahl, die hierfür Ihnen 0 oder 1 zurückgibt.

3. Die Buchung des Nutzers soll nun, sofern erfolgreich, visuell hervorgehoben werden, indem bei einem nunmehr neu reservierten Platz ein „x“, z.B. in der Konsole eingetragen wird. 

   
## Vertiefungsoptionen
Realisieren Sie diese Aufgabe mit einer persistenten Quelle, die es ermöglicht, die Reservierung auch dauerhaft in einem Saal zu speichern. Das zufällige Ausbuchen des Saals sollte in diesem Fall natürlich wegfallen. 

## Hilfestellungen
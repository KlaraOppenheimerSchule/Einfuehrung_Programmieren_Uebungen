# Aufgabe Telefonarten

## Schwierigkeitsgrad: * * * *

## Text der Aufgabe
In dieser Aufgabe betrachten wir verschiedene Arten von Telefonen. Es geht hierbei um den Entwurf einer entsprechenden Klassenhierarchie, mit der die verschiedenen Arten von Telefonen und ihren Komponenten sinnvoll in einem Programm gehandhabt werden können. 
•	Festnetztelefone sind Telefone, die nur an einem bestimmten Standort genutzt werden können, da sie mit dem Festnetz verbunden sind. Für diese Telefone ist der Standort bekannt.

•	Ein Akku speichert seinen Füllstand in Prozent.
•	Bei allen Telefonen wird die Lautstärke ganzzahlig in Dezibel gespeichert.
•	Ein Teil der Festnetztelefone ist stationär, d.h., sie sind fest an einem Standort, wie z.B. der Wohnung oder dem Büro, installiert und können nicht mitgenommen werden.
•	Als Gegensatz zu Festnetztelefonen gibt es Mobiltelefone. Jedes Mobiltelefon benutzt einen Akku als Komponente und die Anzahl der Tasten ist bekannt.
•	Es gibt auch Mobiltelefone mit Touchscreen. Bei diesen kann man die Eingaben per Touchscreen und per Tasten vornehmen. Für diese Telefone ist die Diagonale des Touchscreens bekannt.
•	Die Festnetztelefone, die nicht stationär sind, sind drahtlose Telefone. Solche Telefone können in einem bestimmten Radius um den Standort herum genutzt werden und benutzen einen Akku. Die Reichweite in Metern soll gespeichert werden.
•	Die Akku sind aufladbar und stellen die Methode getLadestand() bereit, mit der der Ladestand (0-100) des Akkus abgefragt werden kann. Außerdem haben sie eine Methode aufladen(), die den Akku auflädt und zurückgibt, ob das Aufladen erfolgreich war.
•	Ein öffentliches Telefon ist ein stationäres Telefon, das jeder benutzen kann. Für dieses Telefon sind die Kosten pro Zeiteinheit in Cent bekannt.

Erstellen Sie hierzu zuerst ein Klassendigramm für die notwendigen Klassen und überführen Sie nach Rücksprache mit Ihrem Lehrer das Klassendiagramm anschließend in einen objektorientierten Code.

## Optionale Erweiterung
Ein Kollege hat Sie darauf hingewiesen, dass es in Zukunft möglich sein soll, unterschiedliche Akkus(Nickel-Kadmium-Akku, Nickel -Metallhydrid-Akkus, Lithium-Ion-Akkus) in den Telefonen mit Akkus einbauen zu können. Weitere Akkuarten werden in der Zukunft sicherlich noch dazu kommen. Jede Akkuart implementiert die Methode aufladen hierbei unterschiedlich. Wichtig ist ihrem Kollegen, dass die Schaffung neuer Akkus keine Änderung im Code der Telefone mit Akku bedarf. Er nannte hierbei das Stichwort „Open-Closed-Prinzip“. Er meinte dies wäre recht solid!?

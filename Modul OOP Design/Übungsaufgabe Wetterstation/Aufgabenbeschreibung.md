# Aufgabe Wetterstation

## Schwierigkeitsgrad:  * * * *

## Aufgabenbeschreibung:
Für eine mit Microcontrollern erstellte Wetterstation sollen Sie einen digitalen Zwilling erstellen. Die Wetterstation besteht auf folgenden Komponenten.
- eine Messstation misst die Temperatur.
- hierfür besteht die Messstation aus einem Microcontroller mit einem angeschlossenen Sensor, der obige Werte erfasst und an den Microcontroller übermittelt.
- Während der Sensor fest mit dem Microcontroller verbunden ist, ist das angeschlossenen Display nur lose mit dem Microcontroller gekoppelt.
- die Messstationen, die aus dem Microcontroller und den dort angeschlossenen Komponenten bestehen, sind jeweils mit der Wetterstation verbunden, die die Daten von verbundenen Messtationen mitteilt und bei Bedarf anzeigt.
- Es sind immer mindestens drei Messstationen vorhanden.
- Die Wetterstation erbt von einer abstrakten Stationsklasse, die lediglich eine StationsID bereithält.
 
![Messstation](https://github.com/KlaraOppenheimerSchule/Einfuehrung_Programmieren_Uebungen/blob/f810656297fc0cded4ca834a53a59e4c19c49777/Modul%20OOP%20Design/%C3%9Cbungsaufgabe%20Wetterstation/Messstation.png)

## Vertiefungsoptionen

1. Die Messstationen übermitteln nun neben der Temperatur auch den Luftdruck und die Luftfeuchtigkeit.
2. Manchmal erfassen die Messstation bei den Temperaturwerten flasche Werte. Implementierungen Sie einen Validiuerungsmechnismus, der sicherstellt, dass die Werte zwischen -40 und + 60 Grad liegen.
3. Erweitern Sie die Applikation dahingehend, dass die Messtationen die Werte nicht unmittelbar an eine Wetterstation weitergibt, sondern dies nach im Sinnes eines MQTT-Brockers umgestezt wird:

Grundprinzip eines MQTT-Brokers:
Publisher: Ein Gerät oder Dienst, das Daten sendet (z. B. ein Temperatursensor).
Subscriber: Ein Gerät oder Dienst, das Daten empfangen möchte (z. B. eine App, die die Temperatur anzeigt).
Broker: Der Vermittler, der Nachrichten vom Publisher entgegennimmt und sie an alle passenden Subscriber weiterleitet.

Wie funktioniert dieser?
Geräte verbinden sich mit dem Broker.
Publisher veröffentlichen Nachrichten zu einem bestimmten Thema (Topic), z. B. sensor/temperatur.
Subscriber abonnieren Themen, die sie interessieren.
Der Broker leitet die Nachrichten automatisch an alle Subscriber weiter, die das entsprechende Thema abonniert haben.

Der Messstation soll insofern eine Klasse vorgeschalten werden, die die Rolle eines Brokers übernimmt.

## Hilfestellungen
Gerne die Lehrkraft ansprechen

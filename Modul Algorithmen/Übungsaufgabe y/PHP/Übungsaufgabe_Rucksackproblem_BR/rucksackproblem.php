<?php

//Laufzeitmessung
$start = microtime(true);

// Tragkraft
$tragkraft = 20;

// Array mit den Gegenstandsbeschreibungen
// Gegenstand,     Wert, Gewicht

$objekte = [
    ["vase",       100,    7 ],
    ["fernseher",  200,    12],
    ["computer",   300,    3 ],
    ["uhr",        150,    10],
];


function rucksackproblem($objekte, $tragkraft)
{
    //Anzahl der Gegenstände
    $n = count($objekte);

    //Maximaler Gesamtwert
    $maximalerGesamtwert = 0;

    //Prüfen aller möglichen Kombinationen
    /*
        1 << $n
        ENTSPRICHT
        1 um n Stellen nach links schieben.

        Wenn n = 4 (vier Gegenstände), dann wird 1 << 4 zu 16, was dasselbe ist wie 2^4.

        in binär bedeutet das also,
        1 << 4
        ENTSPRICHT
        10000(bin)

        Dieses Ergebnis ist die Gesamtanzahl der möglichen Kombinationen der Gegenstände.
        Für vier Gegenstände gibt es 16 Kombinationen:

        (   Keine Gegenstände   0000,
            Ein Gegenstand      0001, 0010, 0100, 1000,
            Zwei Gegenstände    0011, 0101, 0110, 1001, 1010, 1100,
            Drei Gegenstände    0111, 1011, 1101, 1110,
            Vier Gegegenstände  1111).

        $i < (1 << $n) in der For- Schleife bedeutet bei n=4 also das selbe wie $i < 16.
    */
    for ($i = 0; $i < (1 << $n); $i++) {
        $gesamtgewicht = 0;
        $gesamtwert = 0;
        $gegenstandsliste = [];


        for ($j = 0; $j < $n; $j++) {

            /*
             * PERFORMANCE !!! !!!
            if ($gesamtgewicht > $tragkraft) {
                break;
            }*/


            //Vergleich ob in der Kombination gesetzt
            /*
        Die Bedingung if ($i & (1 << $j)) überprüft,
        ob der Gegenstand mit Index $j in der aktuellen Kombination enthalten ist,
        indem sie prüft, ob das $j-te Bit in $
    for ($i = 0; $i < (1 << $n); $i++) {i gesetzt ist.

        Beispiel anhand der ersten Iteration der Schleife:

        Angenommen, $i = 1 (die erste Kombination) und $j = 0 (der erste Gegenstand):
        - $i = 1 in binärer Form ist: 0001
        - $j = 0

        Schritt 1: Erzeugen der Maske (1 << $j)
        - 1 um 0 Stellen nach links schieben:
        - 1 << 0 in binärer Form ist: 0001

        Schritt 2: Bitweise UND-Operation durchführen ($i & (1 << $j))
        - 0001
        - & 0001
        - ----
        - 0001 (das Ergebnis ist ungleich 0, also ist das $j-te Bit in $i gesetzt)

        Das bedeutet, der Gegenstand mit Index 0 ist in der aktuellen Kombination enthalten.

        Wenn $i = 1 und $j = 1 (der zweite Gegenstand):
        - $i = 1 in binärer Form ist: 0001
        - $j = 1

        Schritt 1: Erzeugen der Maske (1 << $j)
        - 1 um 1 Stelle nach links schieben:
        - 1 << 1 in binärer Form ist: 0010

        Schritt 2: Bitweise UND-Operation durchführen ($i & (1 << $j))
        - 0001
        - & 0010
        - ----
        - 0000 (das Ergebnis ist 0, also ist das $j-te Bit in $i nicht gesetzt)

        Das bedeutet, der Gegenstand mit Index 1 ist in der aktuellen Kombination nicht enthalten.
    */
            if ($i & (1 << $j)) {
                $gesamtgewicht += $objekte[$j][2];      // Hinzufügen des Gewichts zum Gesamtgewicht
                $gesamtwert += $objekte[$j][1];         // Hinzufügen des Werts zum Gesamtwert
                $gegenstandsliste[] = $objekte[$j][0];  // Hinzufügen des Gegenstandsnamens zur Liste
            }
        }

        if ($gesamtgewicht <= $tragkraft && $gesamtwert > $maximalerGesamtwert) {
            $maximalerGesamtwert = $gesamtwert;                 // Aktualisieren des Gesamtwerts
            $kombinationsGewicht = $gesamtgewicht;              // Aktualisieren des Gesamtgewichts
            $kombinationsGegenstaende = $gegenstandsliste;      // Aktualisieren der besten Kombination
        }
    }

    return [$maximalerGesamtwert, $kombinationsGegenstaende, $kombinationsGewicht];
}

//Ausgabe des Ergebnisses
$ergebnis = rucksackproblem($objekte, $tragkraft);

echo "Maximaler Gesamtwert: " . $ergebnis[0] . " €\n";
echo "Beste Kombination von Gegenständen: " . implode(", ", $ergebnis[1]). "\n";
echo "Das Gewicht dieser Kombination beträgt " . $ergebnis[2]. "kg\n";


//Zeitmessung
$end = microtime(true);
$time = $end - $start;

echo number_format($time,10)*1000 . " Milisekunden Laufzeit des Skripts";
?>

<?php

// Tragkraft
$T = 20;

// Array mit den Gegenstandsbeschreibungen
// Gegenstand, Wert, Gewicht
$objects = [
    ["vase",        100,     7],
    ["fernseher",   200,    12],
    ["computer",      300,    3],
    ["uhr",         150,    10]
];



function rucksackproblem($objects, $T)
{
    //Anzahl der Gegenstände
    $n = count($objects);

    //Maximaler Gesamtwert
    $G = 0;


    //Prüfen aller möglichen Kombinationen
    /*
        1 << $n
        entspricht
        1 um n Stellen nach links schieben.

        Wenn n = 4 (vier Gegenstände), dann wird 1 << 4 zu 16, was dasselbe ist wie 2^4.

        Das Ergebnis ist die Gesamtanzahl der möglichen Kombinationen der Gegenstände.
        Für vier Gegenstände gibt es 16 Kombinationen:

        (0000,
        0001, 0010, 0100, 1000,
        0011, 0101, 0110, 1001, 1010, 1100,
        0111, 1011, 1101, 1110,
        1111).

        Also sprich $i < (1 << $n) bedeutet das selbe wie $i < 16.
    */



    for ($i = 0; $i < (1 << $n); $i++) {
        $gesamtgewicht = 0;
        $gesamtwert = 0;
        $gegenstandsliste = [];

        for ($j = 0; $j < $n; $j++) {

            /*
            Die Bedingung if ($i & (1 << $j)) überprüft,
            ob der Gegenstand mit Index $j in der aktuellen Kombination enthalten ist,
             indem sie prüft, ob das $j-te Bit in i gesetzt ist.
            */

            if ($i & (1 << $j)) {
                $gesamtgewicht += $objects[$j][2];
                $gesamtwert += $objects[$j][1];
                $gegenstandsliste[] = $objects[$j][0]; // Hinzufügen des Gegenstandsnamens zur Liste
            }
        }

        if ($gesamtgewicht <= $T && $gesamtwert > $G) {
            $G = $gesamtwert;
            $beste_kombination = $gegenstandsliste; // Aktualisieren der besten Kombination
        }
    }

    return [$G, $beste_kombination];
}

$ergebnis = rucksackproblem($objects, $T);

echo "Maximaler Gesamtwert: " . $ergebnis[0] . " €\n";
echo "Beste Kombination von Gegenständen: " . implode(", ", $ergebnis[1]);

?>

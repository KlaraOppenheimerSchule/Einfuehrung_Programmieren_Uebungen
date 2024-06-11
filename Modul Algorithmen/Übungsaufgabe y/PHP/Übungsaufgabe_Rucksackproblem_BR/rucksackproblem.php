<?php

// Tragkraft
$T = 20;

// Array mit den Gegenstandsbeschreibungen
$objects = [
    ["vase",        50,     3],
    ["fernseher",   300,    10],
    ["laptop",      150,    2],
    ["uhr",         400,    7]
];



function rucksackproblem($objects, $T)
{
    //Anzahl der Gegenstände
    $n = count($objects);

    //Maximaler Gesamtwert
    $G = 0;

    for ($i = 0; $i < (1 << $n); $i++) {
        $gesamtgewicht = 0;
        $gesamtwert = 0;
        $gegenstandsliste = [];

        for ($j = 0; $j < $n; $j++) {
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

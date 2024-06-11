<?php

//Tragkraft
$T= 20;


// Wert(€), Gewicht(Kg), Bezeichnung
$vase = [50,3,"vase"];
$fernseher = [300,10,"fernseher"];
$laptop = [150,2,"laptop"];
$uhr = [400,7,"uhr"];

$gewichte = [
    $vase[0],
    $fernseher[0],
    $laptop[0],
    $uhr[0]
];

$werte = [
    $vase[1],
    $fernseher[1],
    $laptop[0],
    $uhr[0]
];




function rucksackproblem($gewichte,$werte,$T)
{
    // n ist die Anzahl an gegenständen
    $n = count($gewichte);

    //bestmögliche Kombination (maximalerGesamtwert)
    $G = 0;

    //Kombinationen durchgehen

    // WENN Kombinationswert Größer als $G UND kleiner als $T,
    // DANN $G = Kombinationswert

    return $G;

}

echo rucksackproblem($gewichte,$werte,3);
<?php

function ggT (int $num1, int $num2)
{


    /* Diese Abfrage ist unnötig, da bei der Teilung unten das zwischenergebnis die kleinere Zahl ist und bei Rekursion
     * wieder die richtige Zahlenreihenfolge verwendet wird
     * if ($num1 < $num2) {
        echo "Big number is smaller than small number, please enter correct values";
    }*/

    if ($num1 == 0 ) {
        return "Der ggT ist: ". $num2;
    }
    if ($num2 == 0 ) {
        return "der ggT ist: ". $num1;
    }


    $intermediateResult= $num1-floor($num1/$num2)*$num2 ;
    echo "Intermediate result: ".$intermediateResult . "\n";

    $num1 = $num2;
    echo "new Big Number is ".$num1 . "\n";

    $num2 = $intermediateResult;
    echo "new small Number is ".$num2 . "\n";

    if ($intermediateResult > 0) {
        echo "loop" . "\n";
        ggT($num1,$num2);
    }
    else echo "Der ggT der beiden Zahlen beträgt: " . $num1;

    //
    /*

      ZwischenErgebnis =  Große Zahl - Wie oft sie reinpasst *  Kleine Zahl
      kleine Zahl = Große Zahl
      Große Zahl =  Zwischenergebnis

      solange ZwischenErgebnis > 0 ggt(grosse Zahl, kleine zahl)

    */


};

echo ggt(450,120);
<?php

class Mathe{

    public static function summe(int $a, int $b):int{

        return $a+$b;
    }

    public static function quadratzahl(int $a){
        return $a*$a;
    }

    public static function obPositiv(int $a){

        if($a>0) return true;

        return false;
    }

    public static function fakultaet(int $a){

        $f = 1;
        for($i=1;$i<=$a;$i++){

            $f = $f *$i;
        }
        return $f;
    }

}

function execSumme(){

    $a = readline('Zahl 1 eingeben: '); 
    $b = readline('Zahl 2 eingeben: '); 
    $result = Mathe::summe($a,$b);
    print $result;echo "\n";
}

function execObPositiv(){

    $a = readline('Zahl eingeben: '); 
    $result = Mathe::obPositiv($a);
    print $result;echo "\n";
}

function execQuadratzahl(){

    $a = readline('Zahl eingeben: '); 
    $result = Mathe::quadratzahl($a);
    print $result;echo "\n";
}

function execfakultaet(){

    $a = readline('Zahl  eingeben: '); 
    $result = Mathe::fakultaet($a);
    print $result;echo "\n";
}


// echo "\n";
echo "1- Summe \n";
echo "2- Quadratzahl \n";
echo "3- Ob Positiv \n";
echo "4- Fakultät \n";

$menu = readline('Menu auswhälen: '); 

switch($menu){
    case "1": execSumme();
    break;
    case "2": execQuadratzahl();
    break;
    case "3": execObPositiv();
    break;
    case "4": execfakultaet();
    break;
    default: echo "Tschüss";
}
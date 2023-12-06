<?php

class MyClass {
    public function addition ($a,$b){
        return $a + $b;
    }
    public function square($a) {
        return $a*$a;
    }
    public function isPositive($a) {
        if ($a >= 0) {
            return true;
        } else return false;
    }
    public function faculty($a) {

        if ($a == 0 || $a == 1){
            return 1;
        } else {
            $fakultaet = 1;
            for ($i = 2; $i <= $a; $i++) {
                $fakultaet *= $i;
            }
            return $fakultaet;
        }

    }
    public function fibonacci($a){

        if ($a <= 1) {
            return 1;
        } else

            $fibarray = array(1,1);
            $pos1 = 0;
            $pos2 = 1;

            for ($i=2;$i<$a;$i++){
            $val1 = $fibarray[$pos1];
            $val2 = $fibarray[$pos2];
            $newval = $val1+$val2;

            $fibarray[] = $newval;

            $pos1++ ;
            $pos2++ ;


            }

            return $fibarray[$a-1];

    }
}


$Klaus = new MyClass();

echo "Die Fiboaccizahl an stelle 600 ist:" . $Klaus->fibonacci(600);
?>


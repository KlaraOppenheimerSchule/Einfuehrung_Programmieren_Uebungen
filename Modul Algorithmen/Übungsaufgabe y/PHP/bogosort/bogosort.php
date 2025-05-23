<?php
function randomiseArray($array):array {

    for($i = 0; $i < count($array); $i++) {
        $temp = $array[$i];
        $random_index = rand(0, (count($array)-1));

        $array[$i]=$array[$random_index];
        $array[$random_index]=$temp;
    }

    return $array;
}
function checkIfArrayIsSorted($array):bool
{
    $sorted = true;
    for ($i = 0; $i < count($array) - 1; $i++) {
        if ($array[$i] > $array[$i + 1]) {
            $sorted = false;
        }
    }
    if ($sorted == true) {
        return true;
    } else {
        return false;
    }
}
function bogosort($array):array {


    $sorted = false;
    $iteration = 0;


    while ($sorted ==false){
        $array= randomiseArray($array);
        $isSorted = checkIfArrayIsSorted($array);

        $sorted = $isSorted;
        $iteration++;
        echo $iteration."\n";
    }

    return $array;


}





$array = [1,4,3,5,73,7,9,2,76,25];
$result = bogosort($array);

var_dump($result);
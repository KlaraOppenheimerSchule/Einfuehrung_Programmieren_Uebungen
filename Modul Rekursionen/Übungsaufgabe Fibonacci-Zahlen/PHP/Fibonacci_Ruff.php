<?php
function fibonacci ($n) {

    if ($n==0 ||$n ==1) {
        return $n;
    }
    else return fibonacci($n-1) + fibonacci($n-2);
}

echo fibonacci(40);
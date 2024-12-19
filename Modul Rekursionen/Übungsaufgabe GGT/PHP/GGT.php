<?php

function ggT($zahlA, $zahlB) : int {
    
    if($zahlB == 0) return $zahlA;
    if($zahlA > $zahlB) return ggT($zahlB, $zahlA % $zahlB);
    else return ggT($zahlA, $zahlB % $zahlA);
}

echo ggt(12, 18);
<?php

namespace Fuhrpark;

class Firebird extends Rennwagen
{
    private int $wattanzahlUnterbodenbeleuchtung;

    public function __construct(int $wattanzahlUnterbodenbeleuchtung,string $hersteller,int $autoID)
    {
        parent::__construct($hersteller, $autoID);
    }

    public function fahren(): void
    {
        echo "Brummbrumm";
    }
}
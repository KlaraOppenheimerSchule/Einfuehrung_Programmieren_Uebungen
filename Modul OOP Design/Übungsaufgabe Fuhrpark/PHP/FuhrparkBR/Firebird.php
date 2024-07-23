<?php

namespace Fuhrpark;

class Firebird extends Rennwagen
{
    private int $wattanzahlUnterbodenbeleuchtung;

    public function __construct(int $wattanzahlUnterbodenbeleuchtung,string $hersteller,int $autoID)
    {
        $this->wattanzahlUnterbodenbeleuchtung = $wattanzahlUnterbodenbeleuchtung;
        parent::__construct($hersteller, $autoID);
    }


    public function getWattanzahlUnterbodenbeleuchtung(): int {
        return $this->wattanzahlUnterbodenbeleuchtung;
    }


    public function fahren(): void
    {
        echo "Brummbrumm";
    }
}
<?php

namespace Fuhrpark\Rennwagen;

use Fuhrpark\Rennwagen;

class MajoretteTurbo extends Rennwagen
{
    private int $anzahlFluegeltueren;


    public function __construct(int $anzahlFluegeltueren, string $hersteller, int $autoID)
    {
        $this->anzahlFluegeltueren = $anzahlFluegeltueren;
        parent::__construct($hersteller, $autoID);
    }


    public function getAnzahlFluegeltueren(): int
    {
        return $this->anzahlFluegeltueren;
    }


    public function fahren(): void
    {
        echo "Uuhweemmn";
    }

}
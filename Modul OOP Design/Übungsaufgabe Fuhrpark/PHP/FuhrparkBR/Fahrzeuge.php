<?php

namespace Fuhrpark;

class Fahrzeuge
{
    public string $hersteller;
    private int $autoID;


    public function __construct(string $hersteller, int $autoID){
        $this->hersteller = $hersteller;
        $this->autoID = $autoID;
    }

    public function getAutoID(): int {
        return $this->autoID;
    }

    public function fahren(): void {
        echo "Fahrzeuge";
    }

}
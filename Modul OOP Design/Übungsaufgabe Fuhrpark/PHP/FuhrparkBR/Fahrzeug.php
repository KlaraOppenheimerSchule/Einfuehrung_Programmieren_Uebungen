<?php

namespace Fuhrpark;

class Fahrzeug
{
    public string $hersteller;
    private int $autoID = 0;


    public function __construct(string $hersteller, int $autoID){
        $this->hersteller = $hersteller;
        $this->autoID = $autoID;
    }

    public function getAutoID(): int {
        return $this->autoID;
    }

    public function setAutoID(int $autoID): void {
        $this->autoID = $autoID;
    }
    public function fahren(): void {
        echo "Fahrzeug";
    }

}
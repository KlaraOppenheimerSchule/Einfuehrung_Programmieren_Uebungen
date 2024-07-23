<?php

namespace Fuhrpark;

class Freizeitwagen extends Fahrzeug
{
    private bool $minibar;


    public function __construct(bool $minibar,string $hersteller, int $autoID)
    {

        $this->minibar = $minibar;
        parent::__construct($hersteller,$autoID);

    }


    public function hasMinibar(): bool
    {
        return $this->minibar;
    }

}
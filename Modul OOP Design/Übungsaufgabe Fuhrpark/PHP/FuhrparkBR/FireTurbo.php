<?php

namespace Fuhrpark;

class FireTurbo extends Rennwagen
{
    private bool $turboAktiviert;

    public function __construct(int $turboAktiviert,string $hersteller,int $autoID)
    {
        $this->turboAktiviert = $turboAktiviert;
        parent::__construct($hersteller, $autoID);
    }


    public function getTurboAktiviert(): bool {
        return $this->turboAktiviert;
    }


    public function fahren(): void
    {
        echo "Brummbrumm";
    }
}
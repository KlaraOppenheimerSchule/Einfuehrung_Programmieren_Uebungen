<?php

namespace Fuhrpark\Freizeitwagen;

use Fuhrpark\Freizeitwagen;

class MercedesBenzAMG extends Freizeitwagen
{

    private bool $wegfahrsperre;


    public function __construct
    (
        bool $wegfahrsperre,
        string $hersteller,
        int $autoID,
        bool $minibar
    )

    {
        $this->wegfahrsperre = $wegfahrsperre;
        parent::__construct($minibar,$hersteller,$autoID);
    }


    public function getWegfahrsoerre(): bool
    {
        return $this->wegfahrsperre;
    }


    public function fahren(): void
    {
        echo "scheeechuiehh";
    }
}
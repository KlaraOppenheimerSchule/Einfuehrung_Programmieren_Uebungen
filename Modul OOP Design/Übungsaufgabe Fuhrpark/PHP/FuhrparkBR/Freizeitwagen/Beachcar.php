<?php

namespace Fuhrpark\Freizeitwagen;

use Fuhrpark\Freizeitwagen;
use Fuhrpark\Lowrider\Lowrider;

class Beachcar extends Freizeitwagen implements Lowrider
{
    private bool $sonnenschutzAusklappbar;


    public function __construct(bool $sonnenschutzAusklappbar,string $hersteller, int $autoID, bool $minibar)
    {

        $this->sonnenschutzAusklappbar = $sonnenschutzAusklappbar;
        parent::__construct($minibar, $hersteller,$autoID);

    }


    public function hasSonnenschutzAusklappbar(): bool
    {
        return $this->sonnenschutzAusklappbar;
    }
    public function jump() : void
    {
       echo "JumpJump";
    }
    public function fahren() : void
    {
      echo "scheeechuiehh";
    }
}
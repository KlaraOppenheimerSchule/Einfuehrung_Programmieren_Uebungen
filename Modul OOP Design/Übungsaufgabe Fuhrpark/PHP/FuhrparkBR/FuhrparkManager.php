<?php

namespace Fuhrpark;

use Fuhrpark\Lowrider\Lowrider;

class FuhrparkManager
{
    private static $instance = null;
    private array $fahrzeuge = [];
    private int $aktuelleAutoID = 0;


    private function __construct() {}


    public static function getInstance() {
        if (self::$instance === null) {
            self::$instance = new FuhrparkManager();
        }
        return self::$instance;
    }


    public function addAuto(Fahrzeug $fahrzeug) {
        $this->aktuelleAutoID++;
        $fahrzeug->setAutoID( $this->aktuelleAutoID);

        $this->fahrzeuge[] = $fahrzeug;
    }

    public function checkFuhrpark()
    {
        foreach ($this->fahrzeuge as $fahrzeug) {
            echo "Auto ID " . $fahrzeug->getAutoID() . ": " . $fahrzeug->fahren() . "\n";
        }
    }
    public function checkFuhrparkJump()
    {
        foreach ($this->fahrzeuge as $fahrzeug) {

            if ($fahrzeug instanceof Lowrider)
                echo " Auto ID: " . $fahrzeug->getAutoID()  . $fahrzeug->jump() . "\n";
        }
    }
}
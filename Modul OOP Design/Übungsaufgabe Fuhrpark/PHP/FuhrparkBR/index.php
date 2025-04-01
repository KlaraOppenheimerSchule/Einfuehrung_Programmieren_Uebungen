<?php

require_once (__DIR__.'/../../vendor/autoload.php');

use Fuhrpark\FuhrparkManager;
use Fuhrpark\Freizeitwagen\MercedesBenzAMG;
use Fuhrpark\Freizeitwagen\Beachcar;
use Fuhrpark\Rennwagen\Firebird;

$fuhrparkManager = FuhrparkManager::getInstance();

$mercedes = new MercedesBenzAMG(true, 'Mercedes', 0, true);
$firebird = new Firebird(350,'Firebird',0);
$beachcar = new Beachcar(true,'Beachcar',0, true);

$fuhrparkManager->addAuto($mercedes);
$fuhrparkManager->addAuto($firebird);
$fuhrparkManager->addAuto($beachcar);

$fuhrparkManager->checkFuhrpark();
$fuhrparkManager->checkFuhrparkJump();
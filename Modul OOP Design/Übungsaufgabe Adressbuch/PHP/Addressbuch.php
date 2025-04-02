<?php

class Kontakt
{
    public string $vorname, $nachname, $telnummer;
    public int $id;

    public function __construct($vorname, $nachname, $telnummer, $id)
    {
        $this->vorname = $vorname;
        $this->nachname = $nachname;
        $this->telnummer = $telnummer;
        $this->id = $id;
    }
}

abstract class Adressbuch
{
    protected array $Kontaktliste;

    public function __construct(Kontakt &$neuerKontakt)
    {
        $this->Kontaktliste = [$neuerKontakt->id => $neuerKontakt];
    }

    public function kontaktHinzufügen(Kontakt &$kontakt): bool
    {
        try {
            $this->Kontaktliste[$kontakt->id] = $kontakt;
            return true;
        } catch (Exception) {
            return false;
        }
    }

    public function kontaktEntfernen(int $id): bool
    {
        try {
            unset($this->Kontaktliste[$id]);
            return true;
        } catch (Exception) {
            return false;
        }
    }
    

    abstract public function gebeKontaktAus(int $id): string;
}


class GeheimesAdressbuch extends Adressbuch {

    public function gebeKontaktAus(int $id): string
    {
        try {
            $kontakt = $this->Kontaktliste[$id];
            return $kontakt->vorname . ": " . $kontakt->telnummer . "\n";
        } catch (Exception $e) {
            return $e->getMessage();
        }
    }

    public function __destruct(){
        foreach($this->Kontaktliste as &$kontakt){
            unset($kontakt);
        }
    }
}

class PrivatesAdressbuch extends Adressbuch
{


    public function gebeKontaktAus(int $id): string
    {
        try {
            $kontakt = $this->Kontaktliste[$id];
            return $kontakt->vorname . ": " . $kontakt->telnummer . "\n";
        } catch (Exception $e) {
            return $e->getMessage();
        }
    }
}

class BeruflichesAdressbuch extends Adressbuch
{


    public function gebeKontaktAus(int $id): string
    {
        try {
            $kontakt = $this->Kontaktliste[$id];
            return $kontakt->nachname . ": " . $kontakt->telnummer . "\n";
        } catch (Exception $e) {
            return $e->getMessage();
        }
    }
}

$dh = new Kontakt("Dominik", "Horlemann", "12345678", 42);

$beruf = new BeruflichesAdressbuch($dh);
$secret = new GeheimesAdressbuch($dh);

unset($secret);
echo $beruf->gebeKontaktAus(42);
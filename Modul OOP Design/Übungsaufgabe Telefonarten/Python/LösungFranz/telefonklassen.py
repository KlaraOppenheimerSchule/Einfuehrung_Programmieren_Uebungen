"""Module which contains all Telefon related classes"""

from abc import ABC
from akkuklassen import Akku

class Telefon(ABC):
    """Abstract Class Telefon"""
    def __init__(self, lautstarke: int):
        self._lautstarke = lautstarke

    def get_lautstarke(self):
        """returns lautstarke as Integer"""
        return self._lautstarke

class Festnetz(Telefon, ABC):
    """Abstract Class Festnetz inherits from Telefon"""
    def __init__(self, lautstarke: int, standort: str):
        super().__init__(lautstarke)
        self._standort = standort

    def get_standort(self):
        """returns standort as String"""
        return self._standort

class Stationar(Festnetz):
    """Class Stationär inherits from Festnetz"""

class Offentlich(Stationar):
    """Class Offentlich inherits from Stationar"""
    def __init__(self, lautstarke: int, standort: str, preis: int):
        super().__init__(lautstarke, standort)
        self._preis = preis

    def get_preis(self):
        """returns preis as Integer"""
        return self._preis

class NonStationar(Festnetz):
    """Class NonStationar inherits from Festnetz"""
    def __init__(self, lautstarke: int, standort: str, reichweite: int, akku: Akku):
        super().__init__(lautstarke, standort)
        self._reichweite = reichweite
        self._akku = akku

    def get_reichweite(self):
        """returns reichweite as Integer"""
        return self._reichweite

    def get_akku(self):
        """returns akku as Akku"""
        return self._akku

class Mobil(Telefon):
    """Class Mobil inherits from Telefon"""
    def __init__(self, lautstarke: int, anzahl_tasten: int, akku):
        super().__init__(lautstarke)
        self._anzahl_tasten = anzahl_tasten
        self.akku = akku

class Smartphone(Mobil):
    """Class Smartphone inherits from Mobil"""
    def __init__(self, lautstarke: int, anzahl_tasten: int, akku, diagonale: float):
        super().__init__(lautstarke, anzahl_tasten, akku)
        self._diagonale = diagonale

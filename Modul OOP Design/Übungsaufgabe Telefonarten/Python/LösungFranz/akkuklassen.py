"""Module which contains all akku related classes"""
from abc import ABC, abstractmethod

class Akku(ABC):
    """Abstract Class Akku"""
    def __init__(self, ladung: int):
        super().__init__()
        self._ladung = ladung

    def get_ladestand(self):
        """Method returns -ladung as int"""
        return self._ladung

    @abstractmethod
    def aufladen(self):
        """Method charges phone, returns boolean (True) when succesfull"""

class LithiumIon(Akku):
    """Class LithiumIon inhertis from Akku"""
    def __init__(self, ladung: int):
        super().__init__(ladung)

    def aufladen(self):
        while self._ladung < 100:
            self._ladung += 0.5
        return self._ladung >= 100

class NickelMetallhydrid(Akku):
    """Class class NickelMetallhydrid inhertis from Akku"""
    def __init__(self, ladung: int):
        super().__init__(ladung)

    def aufladen(self):
        while self._ladung < 100:
            self._ladung += 2
        return self._ladung >= 100

class NickelKadium(Akku):
    """Class NickelKadium inhertis from Akku"""
    def __init__(self, ladung: int):
        super().__init__(ladung)

    def aufladen(self):
        while self._ladung < 100:
            self._ladung += 1
        return self._ladung >= 100

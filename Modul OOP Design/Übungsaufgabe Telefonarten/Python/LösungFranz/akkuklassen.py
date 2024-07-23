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
        for i in 100:
            if i >= 100:
                return True
        return False

class LithiumIon(Akku):
    """Class LithiumIon inhertis from Akku"""
    def aufladen(self):
        for i in range(0, 100, 0.5):
            if i >= 100:
                return True
        return False

class NickelMetallhydrid(Akku):
    """Class class NickelMetallhydrid inhertis from Akku"""
    def aufladen(self):
        for i in range(0, 100, 0.5):
            if i >= 100:
                return True
        return False

class NickelKadium(Akku):
    """Class NickelKadium inhertis from Akku"""
    def aufladen(self):
        for i in range(0, 100, 0.5):
            if i >= 100:
                return True
        return False

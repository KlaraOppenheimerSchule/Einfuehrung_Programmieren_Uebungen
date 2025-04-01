from abc import ABC, abstractmethod

class Kontakt:
    def __init__(self, vorname, nachname, telefonnummer, id):
        self.__vorname = vorname
        self.__nachname = nachname
        self.__telefonnummer = telefonnummer
        self.__id = id

    def getVorname(self):
        return self.__vorname
    
    def getNachname(self):
        return self.__nachname



class AddressBook(ABC):
    def __init__(self):
        self.kontakte = []

    def kontaktHinzufuegen(self, neuerKontakt):
        self.kontakte.append(neuerKontakt)

    def kontaktEntfernen(self, zuEntfernenderKontakt):
        self.kontakte.remove(zuEntfernenderKontakt)

    @abstractmethod
    def gebeKontakteAus(self):
        pass


class PrivateAddressBook(AddressBook):
    def __init__(self):
        super().__init__()

    def gebeKontakteAus(self):
        for kontakt in self.kontakte:
            print(kontakt.getVorname())


class BusinessAddressBook(AddressBook):
    def __init__(self):
        super().__init__()

    def gebeKontakteAus(self):
          for kontakt in self.kontakte:
            print(kontakt.getNachname())


if __name__ == '__main__':
    privatesAdressBuchChristoph = PrivateAddressBook()
    businessAdressBuchChristoph = BusinessAddressBook()

    privatesAdressBuchChristoph.kontaktHinzufuegen(Kontakt("Karl","Steinam", "09317908182",1))
    businessAdressBuchChristoph.kontaktHinzufuegen(Kontakt("Karl","Steinam", "09317908182",1))

    privatesAdressBuchChristoph.gebeKontakteAus()

    businessAdressBuchChristoph.gebeKontakteAus()
